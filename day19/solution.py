import functools
import itertools
import operator
import re
from dataclasses import dataclass
from typing import Literal

ParamName = Literal["x", "m", "a", "s"]
Op = Literal["lt", "gt"]


@dataclass
class Condition:
    param_name: ParamName
    op: Op
    value: int

    def check(self, part: "Part") -> bool:
        match self.op:
            case "lt":
                func = operator.lt
            case "gt":
                func = operator.gt
        return func(part[self.param_name], self.value)

    def inverted(self) -> "Condition":
        match self.op:
            case "lt":
                inverted_op = "gt"
                inverted_value = self.value - 1
            case "gt":
                inverted_op = "lt"
                inverted_value = self.value + 1
        return Condition(
            param_name=self.param_name,
            op=inverted_op,
            value=inverted_value,
        )


Accepted = Literal["A"]
Rejected = Literal["B"]


@dataclass
class Rule:
    target: str | Accepted | Rejected
    condition: Condition | None


@dataclass
class Workflow:
    name: str
    rules: list[Rule]


Part = dict[ParamName, int]


def parse_input(inp: str) -> tuple[list[Workflow], list[Part]]:
    workflow_str, parts_str = inp.split("\n\n")

    workflow_re = re.compile(r"(\w+)\{(.+)\}")
    conditional_rule_re = re.compile(r"([xmas])([<>])(\d+):(\w+)")
    workflows: list[Workflow] = []
    for line in workflow_str.splitlines():
        m = workflow_re.match(line)
        assert m, line
        workflow = Workflow(name=m.group(1), rules=[])
        rules_str = m.group(2)
        for rule in rules_str.split(","):
            if rule_match := conditional_rule_re.match(rule):
                workflow.rules.append(
                    Rule(
                        target=rule_match.group(4),
                        condition=Condition(
                            param_name=rule_match.group(1),  # type: ignore
                            op="lt" if rule_match.group(2) == "<" else "gt",
                            value=int(rule_match.group(3)),
                        ),
                    )
                )
            else:
                workflow.rules.append(Rule(target=rule, condition=None))
        workflows.append(workflow)

    parts: list[Part] = []
    for line in parts_str.splitlines():
        part: Part = {}
        for param_str in line.removeprefix("{").removesuffix("}").split(","):
            param_name, value = param_str.split("=")
            part[param_name] = int(value)  # type: ignore
        parts.append(part)

    return workflows, parts


def part_1(inp: str, debug: bool):
    workflows, parts = parse_input(inp)
    if debug:
        print(*workflows, sep="\n")
        print()
        print(*parts, sep="\n")

    workflow_by_name = {w.name: w for w in workflows}
    rejected: list[Part] = []
    accepted: list[Part] = []
    for part in parts:
        workflow = workflow_by_name["in"]
        while True:
            target: str | None = None
            for rule in workflow.rules:
                if rule.condition is None or rule.condition.check(part):
                    target = rule.target
                    break
            assert target is not None
            match target:
                case "A":
                    accepted.append(part)
                    break
                case "R":
                    rejected.append(part)
                    break
                case next_workflow_name:
                    workflow = workflow_by_name[next_workflow_name]
    if debug:
        print("Accepted:")
        print(*accepted, sep="\n")
        print("Rejected:")
        print(*rejected, sep="\n")

    print(sum(sum(part.values()) for part in accepted))


# assume full dict with 2-element lists always
Bounds = dict[ParamName, list[int]]


def with_condition(bounds: Bounds, condition: Condition) -> Bounds:
    param_bounds = bounds[condition.param_name].copy()
    value_idx = 0 if condition.op == "gt" else 1
    choose_value = max if condition.op == "gt" else min
    param_bounds[value_idx] = choose_value(param_bounds[value_idx], condition.value)
    modified = bounds.copy()
    modified[condition.param_name] = param_bounds
    return modified


def accepted_bounds(
    workflows: dict[str, Workflow],
    start: str,
    initial_bounds: Bounds,
) -> list[Bounds]:
    result: list[Bounds] = []
    workflow = workflows[start]
    for rule in workflow.rules:
        if rule_condition := rule.condition:
            matching = with_condition(initial_bounds, rule_condition)
            kept: Bounds | None = with_condition(initial_bounds, rule_condition.inverted())
        else:
            matching = initial_bounds
            kept = None

        match rule.target:
            case "A":
                result.append(matching)
            case "R":
                pass
            case target_workflow_name:
                result.extend(
                    accepted_bounds(
                        workflows,
                        start=target_workflow_name,
                        initial_bounds=matching,
                    )
                )
        if kept is None:
            break
        else:
            initial_bounds = kept
    return result


def part_2(inp: str, debug: bool):
    workflows, _ = parse_input(inp)
    initial_condition_set: Bounds = {param_name: [0, 4001] for param_name in ("x", "m", "a", "s")}
    accepted = accepted_bounds(
        {w.name: w for w in workflows},
        start="in",
        initial_bounds=initial_condition_set,
    )
    total_accepted = 0
    for bounds in accepted:
        within_bounds = functools.reduce(
            operator.mul, ((upper - lower - 1) for lower, upper in bounds.values()), 1
        )
        total_accepted += max(within_bounds, 0)

    print(total_accepted)
