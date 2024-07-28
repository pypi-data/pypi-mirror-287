from hrepr import H, J, returns

cystyle = [
    {
        "selector": "node",
        "style": {"background-color": "#800", "label": "data(id)"},
    },
    {
        "selector": "edge",
        "style": {
            "width": 3,
            "line-color": "#ccc",
            "target-arrow-color": "#ccc",
            "target-arrow-shape": "triangle",
            "curve-style": "bezier",
        },
    },
]
cytoscape = J(
    module="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.23.0/cytoscape.esm.min.js"
)
j = cytoscape(
    container=returns(
        H.div(style="width:500px;height:500px;border:1px solid black;")
    ),
    elements=[
        {"data": {"id": "A"}},
        {"data": {"id": "B"}},
        {"data": {"id": "C"}},
        {"data": {"source": "A", "target": "B"}},
        {"data": {"source": "B", "target": "C"}},
        {"data": {"source": "C", "target": "A"}},
    ],
    style=cystyle,
    layout={"name": "cose"},
)
print(j.as_page())
