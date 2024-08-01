import psychoanalyst as ps

class CategoriaInterpretativaComparison(ps.ComparisonAnalysisPipeline):
    specification = ps.ComparativeSpecification(
        "Categoría interpretativa Comparison",
        ["Dirección Email"],
        ["Puntuación estándar"]
    )