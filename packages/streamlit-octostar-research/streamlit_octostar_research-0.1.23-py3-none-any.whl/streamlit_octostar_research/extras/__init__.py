from streamlit_octostar_research.configure import octostar_component_func as _component_func
from streamlit_octostar_research.support import require

@require("key")
@require("path")
@require("name")
@require("nodes")
def create_link_chart(key=None,path=None,name=None,nodes=None,edges=None,draft=True,os_workspace=None):
    component_value = _component_func(
        call='octostar:desktop:extras:createLinkChart',
        replyTo=key,
        args=[{"path": path, "name": name, "nodes": nodes, "edges": edges, "draft": draft, "os_workspace": os_workspace}]
    )
    return component_value

def set_transform_result(result): 
    component_value = _component_func(
        call='octostar:remoteapp:setTransformResult',
        args=[result]
    )
    return component_value

def getRecordsCount(saved_search_idn):
    component_value = _component_func(
        call='octostar:savedSearch:getRecordsCount',
        args=[saved_search_idn]
    )
    return component_value

def getRecordsCountQuery(saved_search_idn):
    component_value = _component_func(
        call='octostar:savedSearch:getRecordsCountQuery',
        args=[saved_search_idn]
    )
    return component_value

def getRecords(saved_search_idn, options):
    """
        Args:
            saved_search_idn: The identifier for the saved search.
            options (dict): A dictionary of options for fetching records, with the following keys:
                - all_columns (list of str): A list of all column names to be fetched.
                - order_by_cols (list of str): A list of column names to order the results by.
                - row_limit (int): The maximum number of rows to fetch.
                - server_page_length (int): The length of the pages on the server side.
    """
    component_value = _component_func(
        call='octostar:savedSearch:getRecords',
        args=[saved_search_idn, options]
    )
    return component_value

def getRecordsQuery(saved_search_idn, options):
    """
        Args:
            saved_search_idn: The identifier for the saved search.
            options (dict): A dictionary of options for fetching records, with the following keys:
                - all_columns (list of str): A list of all column names to be fetched.
                - order_by_cols (list of str): A list of column names to order the results by.
                - row_limit (int): The maximum number of rows to fetch.
                - server_page_length (int): The length of the pages on the server side.
    """
    component_value = _component_func(
        call='octostar:savedSearch:getRecordsQuery',
        args=[saved_search_idn, options]
    )
    return component_value

def getSavedSearchPasteContext(saved_search_idn):
    component_value = _component_func(
        call='octostar:savedSearch:getSavedSearchPasteContext',
        args=[saved_search_idn]
    )
    return component_value
