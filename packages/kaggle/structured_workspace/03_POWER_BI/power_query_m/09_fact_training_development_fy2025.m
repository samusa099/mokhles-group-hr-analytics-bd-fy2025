let
    Source = Csv.Document(
        File.Contents(ProjectRoot & "\\02_CLEAN_DATA\\bi_ready_csv\\09_fact_training_development_fy2025.csv"),
        [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true])
in
    PromotedHeaders
