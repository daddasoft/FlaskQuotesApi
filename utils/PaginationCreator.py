from math import ceil


def PgCreator(QuoteCount, currentPage, perPage):
    currentPage = int(currentPage)
    pageCount = ceil(float(QuoteCount / perPage))
    nextPage = currentPage+1 if currentPage + 1 <= pageCount else None
    prevPage = currentPage-1 if currentPage - \
        1 > 0 and currentPage - 1 < pageCount else None

    return {"pagination": {"nextpage": nextPage,
                           "currentPage": currentPage, "prevPage": prevPage, "pages": pageCount}}
