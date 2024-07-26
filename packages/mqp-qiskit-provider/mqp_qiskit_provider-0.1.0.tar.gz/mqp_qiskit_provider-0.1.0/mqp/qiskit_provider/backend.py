"""MQP Backend Module"""

from typing import List, Optional, Union

from qiskit.circuit import QuantumCircuit  # type: ignore
from qiskit.providers import BackendV2, Options  # type: ignore
from qiskit.qasm2 import dumps as qasm_str  # type: ignore
from qiskit.transpiler import CouplingMap, Target  # type: ignore

from mqp.client import MQPClient, ResourceInfo  # type: ignore

from .job import MQPJob
from .mqp_resources import get_coupling_map, get_target


class MQPBackend(BackendV2):
    """MQP Backend class"""

    def __init__(
        self, name: str, client: MQPClient, resource_info: ResourceInfo = None, **kwargs
    ):
        super().__init__(**kwargs)
        self.name = name
        self.client = client
        _resource_info: ResourceInfo = resource_info or self.client.resource_info(
            self.name
        )

        self._coupling_map = get_coupling_map(_resource_info)
        self._target = get_target(_resource_info)

    @classmethod
    def _default_options(cls) -> Options:
        return Options(
            shots=1024, qubit_mapping=None, calibration_set_id=None, no_modify=False
        )

    @property
    def coupling_map(self) -> CouplingMap:
        return self._coupling_map

    @property
    def target(self) -> Target:
        if self._target is None:
            raise NotImplementedError(f"Target for {self.name} is not available.")
        return self._target

    @property
    def max_circuits(self) -> Optional[int]:
        return None

    def run(
        self,
        run_input: Union[QuantumCircuit, List[QuantumCircuit]],
        shots: int = 10000,
        no_modify: bool = False,
        **options,
    ) -> MQPJob:
        # for now, we only support a single circuit
        assert isinstance(run_input, QuantumCircuit), "For now just one circuit per job"
        _circuit = qasm_str(run_input)
        _circuit_format = "qasm"

        job_id = self.client.submit_job(
            resource_name=self.name,
            circuit=_circuit,
            circuit_format=_circuit_format,
            shots=shots,
            no_modify=no_modify,
        )
        return MQPJob(self.client, job_id)


# circuit=b64encode(pickle_dumps(circuits)).decode(encoding="ascii"),
