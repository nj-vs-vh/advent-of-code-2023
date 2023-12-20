import collections
import itertools
import json
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
            origins=[],  # filled later
        )


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
    def initial(cls, modules: list[Module]) -> "ModulesState":
        return ModulesState(
            flip_flops={m.name: LOW for m in modules if m.type_ == "flip-flop"},
            conjuctions={
                m.name: {origin: LOW for origin in m.origins}
                for m in modules
                if m.type_ == "conjunction"
            },
        )


def push_button(modules: dict[str, Module], state: ModulesState) -> dict[str, list[Signal]]:
    signals_received: dict[str, list[Signal]] = collections.defaultdict(list)
    signals_received[BROADCASTER] = [LOW]

    signal_queue = collections.deque[tuple[str, str, Signal]](
        (BROADCASTER, target, LOW) for target in modules[BROADCASTER].targets
    )
    while signal_queue:
        origin_name, target_name, signal = signal_queue.popleft()
        signals_received[target_name].append(signal)
        target = modules.get(target_name)
        if target is None:
            continue
        origin = modules[origin_name]
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
    modules = [Module.parse(line) for line in inp.splitlines()]
    modules_by_name = {m.name: m for m in modules}
    if debug:
        print(*modules, sep="\n")
        print(modules_by_name, sep="\n")
    for origin in modules:
        for target_name in origin.targets:
            if module := modules_by_name.get(target_name):
                module.origins.append(origin.name)

    state = ModulesState.initial(modules)
    signal_counter: dict[Signal, int] = {LOW: 0, HIGH: 0}
    for _ in range(1000):
        for signal in itertools.chain.from_iterable(push_button(modules_by_name, state).values()):
            signal_counter[signal] += 1
    print(signal_counter[LOW] * signal_counter[HIGH])


def part_2(inp: str, debug: bool):
    modules = [Module.parse(line) for line in inp.splitlines()]
    modules_by_name = {m.name: m for m in modules}
    for origin in modules:
        for target_name in origin.targets:
            if module := modules_by_name.get(target_name):
                module.origins.append(origin.name)

    state = ModulesState.initial(modules)
    for button_press in itertools.count():
        signals_received = push_button(modules_by_name, state)
        if LOW in signals_received["rx"]:
            print(button_press)
            break
