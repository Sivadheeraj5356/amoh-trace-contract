# Trace Contract

Independent proof of work for Amoh's environments and evals hiring lane. A tiny deterministic trajectory checker inspired by the engineering problem of rewarding required steps while rejecting shortcuts. This is not an Amoh integration, clinical model or medical decision tool.

The examples are synthetic data-pipeline tasks, not patient cases. Nothing here diagnoses a patient, recommends treatment, processes health information or implements Amoh's clinical verifier.

## Run

Python 3.10+, no dependencies:

```sh
python3 -m unittest -v
python3 verify.py
```

Ten unit tests cover success, missing required actions, forbidden actions, unknown actions, duplicate actions, events after completion, unfinished and empty traces, and contradictory contracts. The UI is a static illustration of the demo output. Run Python for authoritative results.

## Contract

A case specifies allowed, required and forbidden action names. A trace must complete, include every required action and contain no invalid or repeated action. The binary reward is zero on any violation. No LLM or external service is called.

## Limits

This checks action names and completion only. It does not verify that actions actually happened, validate arguments, enforce step ordering, protect against fabricated traces or prove reward robustness. Trusted environment-side event capture, argument validators, state transitions, domain expert review and adversarial testing would be required for real deployment. Exact duplicate rejection is a chosen demo policy, not a general claim about agent workflows. Clinical task semantics are intentionally out of scope.
