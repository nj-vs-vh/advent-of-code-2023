import collections
import itertools
import json
import math
import re
from dataclasses import asdict, dataclass
from pydoc import ModuleScanner
from typing import ClassVar, Literal

BROADCASTER = "broadcaster"


@dataclass
class Module:
    name: str
    type_: Literal["broadcaster", "flip-flop", "conjunction"]
    targets: list[str]
    origins: list[str]

    MODULE_RE: ClassVar = re.compile(r"^(%|&)?(\w+) -> (.+)$")

    @classmethod
    def parse(cls, line: str) -> "Module":
        m = cls.MODULE_RE.match(line)
        assert m, line
        match m.group(1):
            case None:
                type_ = "broadcaster"
            case "%":
                type_ = "flip-flop"
            case "&":
                type_ = "conjunction"
            case _:
                raise ValueError(f"Failed to parse module from {line!r}")
        return Module(
            name=m.group(2),
            type_=type_,
            targets=[t.strip() for t in m.group(3).split(",")],
            origins=[],  # filled later in parse_system
        )

    @classmethod
    def parse_system(cls, inp: str) -> "ModuleSystem":
        modules_list = [Module.parse(line) for line in inp.splitlines()]
        modules = {m.name: m for m in modules_list}
        for origin in modules_list:
            for target_name in origin.targets:
                if module := modules.get(target_name):
                    module.origins.append(origin.name)
        return modules


ModuleSystem = dict[str, Module]
Signal = bool
LOW: Signal = False
HIGH: Signal = True


@dataclass
class ModulesState:
    flip_flops: dict[str, Signal]
    conjuctions: dict[str, dict[str, Signal]]

    def __hash__(self) -> int:
        return hash(json.dumps(asdict(self), check_circular=False, sort_keys=True))

    @classmethod
    def initial(cls, system: ModuleSystem) -> "ModulesState":
        return ModulesState(
            flip_flops={m.name: LOW for m in system.values() if m.type_ == "flip-flop"},
            conjuctions={
                m.name: {origin: LOW for origin in m.origins}
                for m in system.values()
                if m.type_ == "conjunction"
            },
        )


def push_button(system: ModuleSystem, state: ModulesState) -> dict[str, list[Signal]]:
    signals_received: dict[str, list[Signal]] = collections.defaultdict(list)
    signals_received[BROADCASTER] = [LOW]

    signal_queue = collections.deque[tuple[str, str, Signal]](
        (BROADCASTER, target, LOW) for target in system[BROADCASTER].targets
    )
    while signal_queue:
        origin_name, target_name, signal = signal_queue.popleft()
        signals_received[target_name].append(signal)
        target = system.get(target_name)
        if target is None:
            continue
        origin = system[origin_name]
        if target.type_ == "flip-flop" and signal is LOW:
            flipped = not state.flip_flops[target.name]
            state.flip_flops[target.name] = flipped
            signal_queue.extend((target.name, dest, flipped) for dest in target.targets)
        elif target.type_ == "conjunction":
            state.conjuctions[target.name][origin.name] = signal
            nand = not all(state.conjuctions[target.name].values())
            signal_queue.extend((target.name, next_target, nand) for next_target in target.targets)
    return signals_received


def part_1(inp: str, debug: bool):
    system = Module.parse_system(inp)
    if debug:
        print(*system.values(), sep="\n")

    state = ModulesState.initial(system)
    signal_counter: dict[Signal, int] = {LOW: 0, HIGH: 0}
    for _ in range(1000):
        for signal in itertools.chain.from_iterable(push_button(system, state).values()):
            signal_counter[signal] += 1
    print(signal_counter[LOW] * signal_counter[HIGH])


def part_2(inp: str, debug: bool):
    system = Module.parse_system(inp)
    rx_origins = [m for m in system.values() if "rx" in m.targets]

    # the input has very specific properties, check them here
    assert len(rx_origins) == 1
    rx_origin = rx_origins[0]
    # rx parent must be a NAND gate with multiple inputs
    assert rx_origin.type_ == "conjunction"
    subsystems: list[tuple[str, ModuleSystem]] = []
    for subsystem_target in rx_origin.origins:
        # rx grandparents must be NAND gates with 1 input = simple NOT gates
        assert system[subsystem_target].type_ == "conjunction"
        assert len(system[subsystem_target].origins) == 1
        subsystem: ModuleSystem = dict()
        queue = collections.deque[str]([subsystem_target])
        while queue:
            prev_origin = queue.popleft()
            if prev_origin in subsystem:
                continue
            subsystem[prev_origin] = system[prev_origin]
            queue.extend(system[prev_origin].origins)
        subsystems.append((subsystem_target, subsystem))

    # check that subsystems don't overlap (except for broadcaster), so we can simulate them independently
    for _, subsystem_1 in subsystems:
        for _, subsystem_2 in subsystems:
            if subsystem_1 is subsystem_2:
                continue
            assert set(subsystem_1.keys()).intersection(subsystem_2.keys()) == {BROADCASTER}

    # finding a cycle for each subsection
    periods: list[int] = []
    for target, subsystem in subsystems:
        state = ModulesState.initial(subsystem)
        rx_triggering_steps: list[int] = []
        for step in itertools.count():
            received_signals = push_button(subsystem, state)
            if LOW in received_signals[target]:
                rx_triggering_steps.append(step)
                if len(rx_triggering_steps) > 2:
                    break
        period = rx_triggering_steps[1] - rx_triggering_steps[0]
        # same condition for LCM applicability as in day 8
        assert period == rx_triggering_steps[0] + 1
        periods.append(period)

    print(math.lcm(*periods))
