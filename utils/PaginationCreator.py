from math import ceil
from env import env


def PgCreator(QuoteCount, currentPage, perPage):
    currentPage = int(currentPage)
    pageCount = ceil(float(QuoteCount / int(perPage)))
    nextPage = currentPage+1 if currentPage + 1 <= pageCount else None
    prevPage = currentPage-1 if currentPage - \
        1 > 0 and currentPage - 1 < pageCount else None

    return {"pagination": {"nextpage": nextPage,
                           "currentPage": currentPage, "prevPage": prevPage, "pages": pageCount, "perPage": int(env("paginate") or 5)}}
