let
    RootTable = Excel.CurrentWorkbook(){[Name="ProjectRoot"]}[Content],
    ProjectRoot = Text.From(RootTable{0}[Column1]),
    Source = Csv.Document(
        File.Contents(ProjectRoot & "\02_CLEAN_DATA\analysis_ready\employee_360_fy2025.csv"),
        [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true])
in
    PromotedHeaders
