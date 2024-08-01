import psychoanalyst as ps

class RyffComparison(ps.ComparisonAnalysisPipeline):
    specification = ps.ComparativeSpecification(
        "Ryff Comparison",
        ["Dirección Email"],
        ["Puntuación BP"]
    )