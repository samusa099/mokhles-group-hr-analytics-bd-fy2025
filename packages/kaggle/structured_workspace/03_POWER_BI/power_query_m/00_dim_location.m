let
    Source = Csv.Document(
        File.Contents(ProjectRoot & "\\02_CLEAN_DATA\\bi_ready_csv\\00_dim_location.csv"),
        [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true])
in
    PromotedHeaders
