"""Utilidades de salida e inspeccion del estado del motor RETE."""

from experta import KnowledgeEngine


def print_working_memory(engine: KnowledgeEngine) -> None:
    """Imprime todos los hechos actuales en la memoria de trabajo."""
    print("\n=== Memoria de trabajo ===")
    for fact_id, fact in engine.facts.items():
        print(f"  [{fact_id}] {fact.__class__.__name__}: {dict(fact)}")


def print_agenda(engine: KnowledgeEngine) -> None:
    """Imprime las activaciones pendientes en la agenda."""
    print("\n=== Agenda ===")
    activations = list(engine.agenda.activations)
    if not activations:
        print("  (vacia)")
        return
    for index, activation in enumerate(activations, start=1):
        print(f"  {index}: {activation.rule.__name__} -> hechos {activation.facts}")


def print_working_memory_and_agenda(engine: KnowledgeEngine) -> None:
    """Muestra la memoria de trabajo y la agenda del motor."""
    print_working_memory(engine)
    print_agenda(engine)


def run_step_by_step(engine: KnowledgeEngine) -> None:
    """Ejecuta el motor regla a regla mostrando el estado tras cada disparo.

    Util para depuracion: permite observar exactamente que hechos activan
    cada regla y como evoluciona la memoria de trabajo.
    """
    step = 1
    engine.running = True
    try:
        while engine.running:
            added, removed = engine.get_activations()
            engine.strategy.update_agenda(engine.agenda, added, removed)

            print(f"\n--- Estado antes del paso {step} ---")
            print_working_memory(engine)
            print_agenda(engine)

            activation = engine.agenda.get_next()
            if activation is None:
                break

            print(f"\nDisparando: {activation.rule.__name__}")
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
