import pickle
from collections import deque
from typing import List

import networkx as nx

from ceylon.agent.types.agent_request import AgentJobStepRequest, AgentJobResponse
from ceylon.agent.types.job import JobRequest, JobStatus
from ceylon.ceylon import AgentDetail
from ceylon.workspace.admin import Admin
from ceylon.workspace.worker import Worker

workspace_id = "llm_unit"
admin_port = 8888
admin_peer = "admin"


class Agent(Worker):

    def __init__(self, name: str, role: str):
        super().__init__(
            name=name,
            workspace_id=workspace_id,
            admin_port=admin_port,
            admin_peer=admin_peer,
            role=role
        )

    async def on_message(self, agent_id: "str", data: "bytes", time: "int"):
        data = pickle.loads(data)
        if type(data) == AgentJobStepRequest:
            request: AgentJobStepRequest = data
            if request.worker == self.details().name:
                response = await self.execute_request(request)
                response.job_id = request.job_id
                await self.broadcast(pickle.dumps(response))

    async def execute_request(self, request: AgentJobStepRequest) -> AgentJobResponse:
        raise NotImplemented


class RunnerAgent(Admin):
    jobs: List[JobRequest] = []
    connected_agents: List[AgentDetail] = []
    server_mode = False
    parallel_jobs = 1
    running_jobs = []

    def __init__(self, name=workspace_id, port=admin_port, workers=[], tool_llm=None, server_mode=False,
                 parallel_jobs=1):
        self.server_mode = server_mode
        self.parallel_jobs = parallel_jobs
        self.queue = deque()
        self.llm = tool_llm
        # Create a directed graph to represent the workflow
        self.network_graph = nx.DiGraph()
        self.agent_responses = []
        self.workers = workers
        super().__init__(name, port)

    async def run(self, inputs: "bytes"):
        job = pickle.loads(inputs)
        if type(job) == JobRequest:
            await self.add_job(job)

    async def add_job(self, job: JobRequest):
        job.initialize_graph()
        self.jobs.append(job)

    async def start_job(self):
        if len(self.running_jobs) < self.parallel_jobs:
            for agent in self.connected_agents:
                for job in self.jobs:
                    await job.on_agent_connected("", agent, self.broadcast)
                    self.running_jobs.append(job)
                    if len(self.running_jobs) == self.parallel_jobs:
                        return

    async def on_agent_connected(self, topic: "str", agent: AgentDetail):
        self.connected_agents.append(agent)
        await self.start_job()

    async def on_message(self, agent_id: "str", data: "bytes", time: "int"):
        data = pickle.loads(data)
        if type(data) == AgentJobResponse:
            data: AgentJobResponse = data
            job = self.get_job_by_id(data.job_id)
            if job:
                res = await job.execute_request(data, self.broadcast)
                if res is not None and res.status == JobStatus.COMPLETED:
                    self.jobs.remove(job)
                    self.running_jobs.remove(job)
                    print(f"Job {job.id} completed", len(self.running_jobs))

        await self.start_job()
        if not self.server_mode:
            if len(self.jobs) == 0:
                await self.stop()

    def get_job_by_id(self, job_id: str):
        for job in self.jobs:
            if job.id == job_id:
                return job

    def execute(self, job: JobRequest = None):
        return self.run_admin(pickle.dumps(job or {}), self.workers)
