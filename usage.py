from dash import Dash, Input, Output, html

from dash_signature import Signature  # , Test

app = Dash(__name__)
value_store = ""
app.layout = html.Div(
    [
        Signature(
            id="input_signature",
            value="",
            defaultValue="",
        ),
        html.Button(
            "Simulate DB Get Value",
            style={
                "margin": "10px",
                "padding": "10px",
                "backgroundColor": "lightblue",
                "border": "1px solid black",
            },
            id="store-button",
        ),
        html.Div(
            id="output",
            style={
                "overflowWrap": "anywhere",
                "backgroundColor": "lightgrey",
                "width": "1000px",
            },
        ),
    ],
    id="container",
    style={"width": "600px"},
)


@app.callback(
    Output("output", "children"),
    Input("input_signature", "value"),
)
def update_output(value):
    return f"""Length: {0 if value is None else len(value)}
            {value}"""


@app.callback(
    Output("input_signature", "defaultValue"),
    Input("store-button", "n_clicks"),
)
def store_value(n_clicks):
    if n_clicks is not None and n_clicks > 0:
        return "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNjAwIDI0MCIgd2lkdGg9IjYwMCIgaGVpZ2h0PSIyNDAiPjxwYXRoIGQ9Ik0gMjI1LjAwMCwxNTMuMDAwIEMgMjI5LjUwMCwxNTMuMDAwIDIyOS41MDAsMTUzLjAwMCAyMzQuMDAwLDE1My4wMDAiIHN0cm9rZS13aWR0aD0iNS40MTIiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjM0LjAwMCwxNTMuMDAwIEMgMjQxLjAxNywxNTMuMzA0IDI0MS4wMDAsMTUzLjAwMCAyNDguMDAwLDE1My4wMDAiIHN0cm9rZS13aWR0aD0iMy41NDIiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQ4LjAwMCwxNTMuMDAwIEMgMjUyLjQ4NSwxNTIuMzExIDI1Mi41MTcsMTUyLjgwNCAyNTcuMDAwLDE1Mi4wMDAiIHN0cm9rZS13aWR0aD0iMy41NzciIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjU3LjAwMCwxNTIuMDAwIEMgMjY2Ljk5NCwxNTEuMjcwIDI2Ni45ODUsMTUxLjMxMSAyNzcuMDAwLDE1MS4wMDAiIHN0cm9rZS13aWR0aD0iMi44MTgiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjc3LjAwMCwxNTEuMDAwIEMgMjg1LjUwMCwxNTEuMDAwIDI4NS40OTQsMTUwLjc3MCAyOTQuMDAwLDE1MS4wMDAiIHN0cm9rZS13aWR0aD0iMi44MTQiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjk0LjAwMCwxNTEuMDAwIEMgMjk3LjUwMCwxNTEuMDAwIDI5Ny41MDAsMTUxLjAwMCAzMDEuMDAwLDE1MS4wMDAiIHN0cm9rZS13aWR0aD0iMy41NDIiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjwvc3ZnPg=="


if __name__ == "__main__":
    app.run_server(debug=True)
