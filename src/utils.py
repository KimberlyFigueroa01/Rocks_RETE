"""Output and inspection utilities for the RETE engine state."""

from experta import KnowledgeEngine


def print_working_memory(engine: KnowledgeEngine) -> None:
    """Prints all current facts in the working memory."""
    print("\n=== Working Memory ===")
    for fact_id, fact in engine.facts.items():
        print(f"  [{fact_id}] {fact.__class__.__name__}: {dict(fact)}")


def print_agenda(engine: KnowledgeEngine) -> None:
    """Prints pending activations in the agenda."""
    print("\n=== Agenda ===")
    activations = list(engine.agenda.activations)
    if not activations:
        print("  (empty)")
        return
    for index, activation in enumerate(activations, start=1):
        print(f"  {index}: {activation.rule.__name__} -> facts {activation.facts}")


def print_working_memory_and_agenda(engine: KnowledgeEngine) -> None:
    """Shows the engine's working memory and agenda."""
    print_working_memory(engine)
    print_agenda(engine)


def run_step_by_step(engine: KnowledgeEngine) -> None:
    """Executes the engine rule by rule, showing the state after each firing.

    Useful for debugging: allows observing exactly which facts trigger
    each rule and how the working memory evolves.
    """
    step = 1
    engine.running = True
    try:
        while engine.running:
            added, removed = engine.get_activations()
            engine.strategy.update_agenda(engine.agenda, added, removed)

            print(f"\n--- State before step {step} ---")
            print_working_memory(engine)
            print_agenda(engine)

            activation = engine.agenda.get_next()
            if activation is None:
                break

            print(f"\nFiring: {activation.rule.__name__}")
            activation.rule(
                engine,
                **{
                    key: value
                    for key, value in activation.context.items()
                    if not key.startswith('__')
                }
            )
            step += 1
    finally:
        engine.running = False
