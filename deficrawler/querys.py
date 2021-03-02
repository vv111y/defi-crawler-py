class Querys:
    BORROWS_FROM_TIMESTAMP = {
        "AAVE": """{{
                    borrows(
                            first: 1000
                            orderBy:timestamp
                            orderDirection: asc
                            where: {{
                            timestamp_gt: {}
                            }}
                        ){{
                        user{{
                         id
                        }}
                        reserve{{
                          symbol
                        }}
                        amount
                        timestamp
                    }}
                    }}
                """,
        "COMPOUND": """{{
                        borrowEvents(
                                first: 1000
                                orderBy: blockTime
                                orderDirection:asc
                                where: {{
                                blockTime_gt: {}
                                }}
                            ){{
                            id
                            amount
                            accountBorrows
                            borrower
                            underlyingSymbol
                            blockTime
                        }}
                    }}
                """,
        "MAKER": """
                {{
                vaults(
                    first:1000
                    orderBy: openedAt
                    orderDirection:desc
                        where: {{
                            openedAt_gt: {}
                        }}
                ){{
                    owner{{
                        address
                    }}
                    debt
                    openedAt
                }}
                }}
        """,
        "CREAM": """
            {{
            borrowEvents(
                first:1000
                orderBy:blockTime
                orderDirection:desc
                where: {{
                blockTime_gt:{}
                }}
            ){{
                id
                amount
                accountBorrows
                borrower
                underlyingSymbol
                blockTime
            }}
            }}
    """
    }