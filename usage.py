from dash import Dash, Input, Output, ctx, html

import dash_ijack_components

app = Dash(__name__)
value_store = ""
app.layout = html.Div(
    [
        dash_ijack_components.Signature(
            id="input",
            value="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNjAwIDI0MCIgd2lkdGg9IjYwMCIgaGVpZ2h0PSIyNDAiPjxwYXRoIGQ9Ik0gODkuMzI4LDIwNi43MTUgQyA5NS44MTUsMjAwLjQ2OCA5NS41MzEsMjAwLjIxNSAxMDEuNzM0LDE5My43MTUiIHN0cm9rZS13aWR0aD0iNC43MzYiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTAxLjczNCwxOTMuNzE1IEMgMTExLjI4OSwxODIuMzAxIDExMS41NDAsMTgyLjUyNyAxMjAuNzc3LDE3MC44MzIiIHN0cm9rZS13aWR0aD0iMi4zODUiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTIwLjc3NywxNzAuODMyIEMgMTMzLjUyOCwxNTcuMTAyIDEzMi42NDMsMTU2LjQ4OSAxNDQuNDQxLDE0Mi4wOTAiIHN0cm9rZS13aWR0aD0iMS44NTIiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTQ0LjQ0MSwxNDIuMDkwIEMgMTUwLjUyMiwxMzIuNDU4IDE1MS4xMDgsMTMyLjkxOSAxNTUuOTM4LDEyMi40NjUiIHN0cm9rZS13aWR0aD0iMi4xNTgiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTU1LjkzOCwxMjIuNDY1IEMgMTYxLjg3MiwxMTIuMzg3IDE2MS40NTQsMTEyLjI4NiAxNjYuMzA1LDEwMS43NDYiIHN0cm9rZS13aWR0aD0iMi4zMDkiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTY2LjMwNSwxMDEuNzQ2IEMgMTY3LjgyMyw5Ni4yMzAgMTY4LjQ5Myw5Ni40OTMgMTY5LjE4MCw5MC42NzYiIHN0cm9rZS13aWR0aD0iMi45NTgiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTY5LjE4MCw5MC42NzYgQyAxNzAuMDE0LDg3LjA0OCAxNzAuMDYzLDg3LjA2MCAxNzAuNzg1LDgzLjQwNiIgc3Ryb2tlLXdpZHRoPSIzLjUyNCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAxNzAuNzg1LDgzLjQwNiBDIDE3MS43NTEsODAuMDgwIDE3MS40OTQsODAuMDU3IDE3Mi4xNDEsNzYuNjk1IiBzdHJva2Utd2lkdGg9IjMuODkyIiBzdHJva2U9ImJsYWNrIiBmaWxsPSJub25lIiBzdHJva2UtbGluZWNhcD0icm91bmQiPjwvcGF0aD48cGF0aCBkPSJNIDE3Mi4xNDEsNzYuNjk1IEMgMTcxLjg5NCw3MC4xNjYgMTcyLjQyOCw3NC4xOTkgMTcyLjE0MSw3MS42NDUiIHN0cm9rZS13aWR0aD0iNC42NzYiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTcyLjE0MSw3MS42NDUgQyAxNzIuOTczLDgxLjQ3MyAxNzMuMTAzLDc3LjQwNCAxNzQuNTU5LDkxLjE3MiIgc3Ryb2tlLXdpZHRoPSI0LjQzMSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAxNzQuNTU5LDkxLjE3MiBDIDE3Ni4xOTAsOTcuNzMyIDE3NS42NDcsOTcuODMxIDE3Ny40ODgsMTA0LjM1OSIgc3Ryb2tlLXdpZHRoPSIzLjQzNiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAxNzcuNDg4LDEwNC4zNTkgQyAxODAuNjY0LDEyMS40MjMgMTgwLjgyNSwxMjEuMzkwIDE4My44MjgsMTM4LjQ4OCIgc3Ryb2tlLXdpZHRoPSIyLjIxNCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAxODMuODI4LDEzOC40ODggQyAxODQuOTI0LDE0NC4xMzkgMTg0Ljg3NywxNDQuMTQ3IDE4NS45MTQsMTQ5LjgwOSIgc3Ryb2tlLXdpZHRoPSIyLjg2MSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAxODUuOTE0LDE0OS44MDkgQyAxODUuOTAxLDE1OC44NzIgMTg2LjY3MiwxNTQuMTUxIDE4Ny4zMjQsMTU4LjUxMiIgc3Ryb2tlLXdpZHRoPSIzLjM1NyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAxODcuMzI0LDE1OC41MTIgQyAxOTAuMTMzLDE1My40MjQgMTg5LjE5NiwxNTguMDM4IDE5Mi41MDQsMTQ4LjE0MSIgc3Ryb2tlLXdpZHRoPSI0LjI1NSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAxOTIuNTA0LDE0OC4xNDEgQyAxOTQuMTMyLDE0Mi44MDEgMTk0Ljc1NiwxNDMuMTIzIDE5Ni41NzAsMTM3LjkxMCIgc3Ryb2tlLXdpZHRoPSIzLjYyOSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAxOTYuNTcwLDEzNy45MTAgQyAxOTcuNzY2LDEzNS4yNTIgMTk3Ljc3OCwxMzUuNDg3IDE5OS43OTcsMTMzLjUxMiIgc3Ryb2tlLXdpZHRoPSI0LjAwNyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAxOTkuNzk3LDEzMy41MTIgQyAyMDIuNzA0LDEzMC4yNzUgMjAyLjU0NywxMzEuMTU2IDIwNi4xMzMsMTI5LjcxOSIgc3Ryb2tlLXdpZHRoPSIzLjk0NyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyMDYuMTMzLDEyOS43MTkgQyAyMTEuNDUzLDEyOC43MjcgMjEwLjIyMywxMjkuMDU2IDIxNC44MzYsMTMxLjA3NCIgc3Ryb2tlLXdpZHRoPSIzLjcxOCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyMTQuODM2LDEzMS4wNzQgQyAyMTguOTkwLDEzNi4zNTEgMjE5Ljk5NCwxMzQuNjUzIDIyMy4yMTUsMTQxLjU3MCIgc3Ryb2tlLXdpZHRoPSIzLjI5NSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyMjMuMjE1LDE0MS41NzAgQyAyMjguNzU3LDE0OC40MjggMjI4Ljc2MiwxNDguNDIzIDIzNC4zNzksMTU1LjIxOSIgc3Ryb2tlLXdpZHRoPSIyLjgzNiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyMzQuMzc5LDE1NS4yMTkgQyAyMzYuNzg1LDE1OC40MDQgMjM2LjkxMSwxNTguMjc3IDIzOS41MjMsMTYxLjI3MCIgc3Ryb2tlLXdpZHRoPSIzLjQ2OCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyMzkuNTIzLDE2MS4yNzAgQyAyNDEuODEwLDE2NC4yNzYgMjQxLjk4OCwxNjMuODQ4IDI0NC43ODUsMTY2LjEwNSIgc3Ryb2tlLXdpZHRoPSIzLjc1MiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNDQuNzg1LDE2Ni4xMDUgQyAyNDcuNjIxLDE2OC40NzUgMjQ3LjIxNCwxNjcuNTk5IDI1MC4zMzIsMTY3LjkxNCIgc3Ryb2tlLXdpZHRoPSI0LjA0NyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNTAuMzMyLDE2Ny45MTQgQyAyNTcuMTYyLDE2NS4wNDYgMjU3LjIxNSwxNjYuNDg5IDI2My45NzMsMTYyLjEzMyIgc3Ryb2tlLXdpZHRoPSIzLjk1NiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNjMuOTczLDE2Mi4xMzMgQyAyNjcuNTYzLDE1OS45NjggMjY3LjcyOCwxNjAuNTI2IDI3MS40NjUsMTU4Ljg3NSIgc3Ryb2tlLXdpZHRoPSIzLjc5MCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNzEuNDY1LDE1OC44NzUgQyAyNzYuMTQxLDE1Ny44NzkgMjc2LjAxMiwxNTcuNjAxIDI4MC44NzEsMTU3LjM5OCIgc3Ryb2tlLXdpZHRoPSIzLjYwMiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyODAuODcxLDE1Ny4zOTggQyAyODUuOTYyLDE1Ny4yNjIgMjg1LjkyNiwxNTYuODg1IDI5MS4wMzUsMTU2Ljg4NyIgc3Ryb2tlLXdpZHRoPSIzLjU0MyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyOTEuMDM1LDE1Ni44ODcgQyAyOTYuNTkzLDE1Ni43ODIgMjk2LjUzNCwxNTYuNDgwIDMwMi4wMTYsMTU1LjgzNiIgc3Ryb2tlLXdpZHRoPSIzLjQ1MCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzMDIuMDE2LDE1NS44MzYgQyAzMTAuNTQwLDE1NC40NzUgMzEwLjQ0MiwxNTQuMzY2IDMxOC43MzQsMTUyLjA1NSIgc3Ryb2tlLXdpZHRoPSIyLjkwMSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzMTguNzM0LDE1Mi4wNTUgQyAzMjQuMjgwLDE1MC4yNzAgMzI0LjI2MywxNTAuNDIyIDMyOS40NjEsMTQ3LjczMCIgc3Ryb2tlLXdpZHRoPSIzLjIwMCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzMjkuNDYxLDE0Ny43MzAgQyAzMzUuMzE3LDE0NC41NDYgMzM1LjQyOSwxNDQuODA1IDM0MS4wMzEsMTQxLjEyNSIgc3Ryb2tlLXdpZHRoPSIzLjE2NyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNDEuMDMxLDE0MS4xMjUgQyAzNDUuOTAwLDEzNy44MTQgMzQ2LjA3MSwxMzguMTA3IDM1MC45NjksMTM0Ljg1MiIgc3Ryb2tlLXdpZHRoPSIzLjI3NyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNTAuOTY5LDEzNC44NTIgQyAzNTQuMDI5LDEzMi44MjQgMzU0LjA3OCwxMzMuMDM0IDM1Ny4zODcsMTMxLjU2NiIgc3Ryb2tlLXdpZHRoPSIzLjY3NSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNDguMDQ3LDExMC40MjYgQyAyNTEuNTE0LDExMC40MjYgMjUxLjUxNCwxMTAuNDI2IDI1NC45ODAsMTEwLjQyNiIgc3Ryb2tlLXdpZHRoPSI1LjIwNCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNTQuOTgwLDExMC40MjYgQyAyNjYuOTQzLDExMC40MjYgMjY2Ljk0MywxMTAuNDI2IDI3OC45MDYsMTEwLjQyNiIgc3Ryb2tlLXdpZHRoPSIyLjcxNiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNzguOTA2LDExMC40MjYgQyAyODguODg1LDExMC40MjYgMjg4Ljg4NSwxMTAuNDI2IDI5OC44NjMsMTEwLjQyNiIgc3Ryb2tlLXdpZHRoPSIyLjU2MyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyOTguODYzLDExMC40MjYgQyAzMTMuNDc2LDExMS44MDQgMzEzLjM0NiwxMTAuNDI2IDMyNy44MjgsMTEwLjQyNiIgc3Ryb2tlLXdpZHRoPSIyLjIwNSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzMjcuODI4LDExMC40MjYgQyAzNDMuMjUyLDEwOC45NjIgMzQyLjU1MywxMDkuMDExIDM1Ny4wMTYsMTA0Ljg0MCIgc3Ryb2tlLXdpZHRoPSIyLjY1OSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNTcuMDE2LDEwNC44NDAgQyAzNTkuNDE0LDEwMy4xNDAgMzU5LjM3MSwxMDQuMTM0IDM2MC4wNjYsMTAwLjc3MCIgc3Ryb2tlLXdpZHRoPSIzLjY0MyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNjAuMDY2LDEwMC43NzAgQyAzNjAuNzUzLDk1LjUyNyAzNjEuNDIwLDk1Ljg1MyAzNjEuMDI3LDkwLjI2NiIgc3Ryb2tlLXdpZHRoPSIzLjUyMSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNjEuMDI3LDkwLjI2NiBDIDM2MS4wMjcsODYuMjg5IDM2MS4yMzQsODYuMjk4IDM2MS4wMjcsODIuMzEzIiBzdHJva2Utd2lkdGg9IjMuNjgzIiBzdHJva2U9ImJsYWNrIiBmaWxsPSJub25lIiBzdHJva2UtbGluZWNhcD0icm91bmQiPjwvcGF0aD48cGF0aCBkPSJNIDM2MS4wMjcsODIuMzEzIEMgMzYyLjA5OCw3NS45MDMgMzYxLjAyNyw3OS4wNDMgMzYxLjAyNyw3NS43NzMiIHN0cm9rZS13aWR0aD0iNC4zNTEiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMzYxLjAyNyw3NS43NzMgQyAzNTcuNDk1LDc4LjE5MiAzNTkuNzkwLDc1LjYyNCAzNTYuNDEwLDgxLjc1NCIgc3Ryb2tlLXdpZHRoPSI0LjcxMyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNTYuNDEwLDgxLjc1NCBDIDM1Mi44ODQsOTguMzAyIDM1MS41NTAsOTcuNzA2IDM0OS4xMzcsMTE0LjgwMSIgc3Ryb2tlLXdpZHRoPSIyLjI5NSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNDkuMTM3LDExNC44MDEgQyAzNDMuNTIyLDEzOS43ODUgMzQzLjQ2NiwxMzkuNzY5IDMzNy41NzQsMTY0LjY4OCIgc3Ryb2tlLXdpZHRoPSIxLjU4NyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzMzcuNTc0LDE2NC42ODggQyAzMzUuNjgyLDE3MS45MTcgMzM1LjgzOCwxNzEuOTU1IDMzMy43NzAsMTc5LjE0MSIgc3Ryb2tlLXdpZHRoPSIyLjM2NSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzMzMuNzcwLDE3OS4xNDEgQyAzMjcuOTYwLDIwNy4zOTggMzI2LjQyNiwyMDYuODc0IDMxOS4wNjMsMjM0LjYwMiIgc3Ryb2tlLXdpZHRoPSIxLjQ5MCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzMTkuMDYzLDIzNC42MDIgQyAzMTIuMzAzLDI1My4zMzcgMzEyLjkyMywyNTMuMzc1IDMwMy42OTUsMjcxLjA5NCIgc3Ryb2tlLXdpZHRoPSIxLjYyNCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzMDMuNjk1LDI3MS4wOTQgQyAzMDAuMTc1LDI3OS4zMjAgMzAwLjA0OSwyNzguNjE3IDI5NC41NTUsMjg1LjE2MCIgc3Ryb2tlLXdpZHRoPSIyLjI3NSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyOTQuNTU1LDI4NS4xNjAgQyAyOTAuNjk5LDI4OC4zMzIgMjkxLjUwNCwyODguMzMwIDI4Ni4zNTIsMjg5LjExMyIgc3Ryb2tlLXdpZHRoPSIzLjEzMiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyODYuMzUyLDI4OS4xMTMgQyAyNzkuMTQ5LDI5MS43NjAgMjgxLjA0NywyOTAuMDY3IDI3NS4yNTAsMjg4LjYyOSIgc3Ryb2tlLXdpZHRoPSIzLjI2MSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNzUuMjUwLDI4OC42MjkgQyAyNjkuMDI5LDI4MC4wODcgMjY3Ljg4MywyODIuNzEyIDI2My44MjAsMjcxLjAxNiIgc3Ryb2tlLXdpZHRoPSIyLjcwMiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNjMuODIwLDI3MS4wMTYgQyAyNjEuNzY3LDI2Ny4xMDkgMjYxLjY1OCwyNjcuMjUwIDI2MC41MDgsMjYyLjk1MyIgc3Ryb2tlLXdpZHRoPSIzLjM0MSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNjAuNTA4LDI2Mi45NTMgQyAyNTguNjk5LDI1Ny40ODEgMjU4Ljg2OSwyNTcuNTQzIDI1OC4wMjMsMjUxLjg4MyIgc3Ryb2tlLXdpZHRoPSIzLjI0MyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNTguMDIzLDI1MS44ODMgQyAyNTcuMjI4LDI0Ni45MjggMjU3LjQ1NiwyNDcuMTgyIDI1OC4wMjMsMjQyLjM1NSIgc3Ryb2tlLXdpZHRoPSIzLjQzNiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNTguMDIzLDI0Mi4zNTUgQyAyNTguNTE4LDIzOS4xNTAgMjU4LjQ4NiwyMzkuNjk4IDI2MC41MzksMjM3LjQyMiIgc3Ryb2tlLXdpZHRoPSIzLjkyNCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNjAuNTM5LDIzNy40MjIgQyAyNjUuMTA2LDIzNC44MDggMjY0LjM3OSwyMzQuMTM5IDI2OS43NDYsMjMyLjMzMiIgc3Ryb2tlLXdpZHRoPSIzLjU5OCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNjkuNzQ2LDIzMi4zMzIgQyAyNzIuMzE2LDIzMC43MjcgMjcyLjM5MSwyMzAuOTIxIDI3NS4xMDksMjI5LjY0OCIgc3Ryb2tlLXdpZHRoPSIzLjk3MyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyNzUuMTA5LDIyOS42NDggQyAyODQuMzIzLDIyNi4xNTUgMjg0LjI4MSwyMjYuMTA4IDI5My42NzYsMjIzLjA5NCIgc3Ryb2tlLXdpZHRoPSIyLjkwNiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAyOTMuNjc2LDIyMy4wOTQgQyAzMDAuNTI3LDIyMS4zNjAgMzAwLjM3NiwyMjAuOTAxIDMwNy4yMTUsMjE5LjE0MSIgc3Ryb2tlLXdpZHRoPSIzLjAyMiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzMDcuMjE1LDIxOS4xNDEgQyAzMTIuNjU4LDIxNi45MTEgMzEyLjc4NywyMTcuMjkyIDMxOC4xOTUsMjE0Ljk1NyIgc3Ryb2tlLXdpZHRoPSIzLjIyOSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzMTguMTk1LDIxNC45NTcgQyAzMjEuOTA0LDIxMy43MjAgMzIxLjg3OCwyMTMuNjU3IDMyNS42NTYsMjEyLjYzMyIgc3Ryb2tlLXdpZHRoPSIzLjY0MiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzMjUuNjU2LDIxMi42MzMgQyAzMzAuNDczLDIxMS40NDAgMzMwLjQxOCwyMTEuMjUzIDMzNS4yMjMsMjEwLjAyMyIgc3Ryb2tlLXdpZHRoPSIzLjU3OSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzMzUuMjIzLDIxMC4wMjMgQyAzMzguNjc4LDIwOS4yNDggMzM4LjU1NCwyMDkuMDMwIDM0MS44MTYsMjA3LjgxMyIgc3Ryb2tlLXdpZHRoPSIzLjg1OCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNDEuODE2LDIwNy44MTMgQyAzNDQuMzY0LDIwNi43ODQgMzQ0LjE3MCwyMDYuNzM2IDM0Ni4yMDcsMjA1LjAwMCIgc3Ryb2tlLXdpZHRoPSI0LjExOSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNDYuMjA3LDIwNS4wMDAgQyAzNDguNDM1LDIwMi42MDIgMzQ4LjQ4MywyMDIuNzk4IDM1MC4wNTUsMTk5Ljg0MCIgc3Ryb2tlLXdpZHRoPSI0LjA0MyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNTAuMDU1LDE5OS44NDAgQyAzNTEuOTM0LDE5Ni41NTQgMzUxLjk0MSwxOTYuNjIzIDM1My4yMTksMTkzLjA0MyIgc3Ryb2tlLXdpZHRoPSIzLjk0NCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNTMuMjE5LDE5My4wNDMgQyAzNTUuMDQ4LDE4OC4wMzAgMzU1LjAzOSwxODguMDcwIDM1Ni4yNjYsMTgyLjg3MSIgc3Ryb2tlLXdpZHRoPSIzLjU5NCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNTYuMjY2LDE4Mi44NzEgQyAzNTcuNDE1LDE3Ni45ODEgMzU3LjY0MiwxNzcuMDQyIDM1OC40MDYsMTcxLjA2NiIgc3Ryb2tlLXdpZHRoPSIzLjQzOCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNTguNDA2LDE3MS4wNjYgQyAzNTguNTg0LDE2OC4wMDkgMzU4LjkwNywxNjguMDc1IDM1OS4yNTAsMTY1LjA1OSIgc3Ryb2tlLXdpZHRoPSIzLjkwNSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNTkuMjUwLDE2NS4wNTkgQyAzNTkuNDQ4LDE1OC4zNzkgMzYwLjAyNiwxNjEuNjIyIDM2MS4yODksMTU4LjI5MyIgc3Ryb2tlLXdpZHRoPSI0LjM4NyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNjEuMjg5LDE1OC4yOTMgQyAzNjQuNDQ3LDE2MS40ODUgMzYzLjYyOSwxNTguMTg0IDM2Ny42MTMsMTY0LjY2OCIgc3Ryb2tlLXdpZHRoPSI0LjQxMSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNjcuNjEzLDE2NC42NjggQyAzNjkuMDIxLDE2Ny4wNDQgMzY5LjM5NCwxNjYuNDU4IDM3MS4xODQsMTY4LjIzOCIgc3Ryb2tlLXdpZHRoPSI0LjMxNiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNzEuMTg0LDE2OC4yMzggQyAzNzYuNDE5LDE3Mi44NDAgMzc1LjEyOCwxNzAuNDE2IDM3OS44MjgsMTcxLjQxMCIgc3Ryb2tlLXdpZHRoPSI0LjM1MiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzNzkuODI4LDE3MS40MTAgQyAzODMuNzE2LDE2Ni43MDUgMzg0LjMyMiwxNjkuNTI1IDM4Ni45ODgsMTYxLjYwOSIgc3Ryb2tlLXdpZHRoPSI0LjE1NyIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzODYuOTg4LDE2MS42MDkgQyAzODguMzIwLDE1NS44NjUgMzg5LjcxNiwxNTcuMzYzIDM5MS44MjgsMTUyLjcyNyIgc3Ryb2tlLXdpZHRoPSI0LjMwMCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzOTEuODI4LDE1Mi43MjcgQyAzOTUuNzc5LDE1MC4wMzIgMzk0Ljc3OSwxNTAuMDg3IDM5OS45MDYsMTUwLjA1NSIgc3Ryb2tlLXdpZHRoPSI0LjQ1NSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSAzOTkuOTA2LDE1MC4wNTUgQyA0MDcuMTY3LDE1MS40OTkgNDA3LjA4OCwxNTAuMDk0IDQxNC40NDUsMTUyLjg1MiIgc3Ryb2tlLXdpZHRoPSI0LjAzOCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSA0MTQuNDQ1LDE1Mi44NTIgQyA0MTguMzg0LDE1My44NjUgNDE4LjQxMCwxNTMuNTg5IDQyMi4zOTEsMTU0LjIzNCIgc3Ryb2tlLXdpZHRoPSIzLjg3OSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSA0MjIuMzkxLDE1NC4yMzQgQyA0MjguNTI0LDE1NC41NjQgNDI4LjQ5MSwxNTQuNzk3IDQzNC42NjAsMTU0LjcxNSIgc3Ryb2tlLXdpZHRoPSIzLjM2NCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSA0MzQuNjYwLDE1NC43MTUgQyA0MzguMzEzLDE1NS4wNTIgNDM4LjI4MCwxNTQuODA0IDQ0MS45MDIsMTU0LjcxNSIgc3Ryb2tlLXdpZHRoPSIzLjcwNCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSA0NDEuOTAyLDE1NC43MTUgQyA0NDUuNTE3LDE1My45OTcgNDQ1LjU1NSwxNTQuMzcyIDQ0OS4xNDUsMTUzLjM1NSIgc3Ryb2tlLXdpZHRoPSIzLjgwNiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSA0NDkuMTQ1LDE1My4zNTUgQyA0NTMuNTE0LDE1Mi44NDAgNDUzLjQ2MiwxNTIuNTkyIDQ1Ny43OTMsMTUxLjkwNiIgc3Ryb2tlLXdpZHRoPSIzLjczOSIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSA0NTcuNzkzLDE1MS45MDYgQyA0NjIuODEwLDE1MS40MTkgNDYyLjU0MSwxNTAuODcwIDQ2Ny4xOTksMTQ5LjQxNCIgc3Ryb2tlLXdpZHRoPSIzLjYyNCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PHBhdGggZD0iTSA0NjcuMTk5LDE0OS40MTQgQyA0NzUuMjA4LDE0Ni4wODIgNDc0LjgwMiwxNDUuOTQxIDQ4MS43NzcsMTQwLjk0OSIgc3Ryb2tlLXdpZHRoPSIyLjk1NiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48L3BhdGg+PC9zdmc+",
        ),
        html.Button(
            "Clear",
            id="clear-button",
            style={"padding": "10px", "backgroundColor": "red"},
        ),
        html.Button(
            "Save",
            id="save-button",
            style={"padding": "10px", "backgroundColor": "green"},
        ),
        html.Button(
            "Store",
            id="store-button",
            style={"padding": "10px", "backgroundColor": "blue"},
        ),
        html.Button(
            "Restore",
            id="restore-button",
            style={"padding": "10px", "backgroundColor": "yellow"},
        ),
        html.Div(
            id="output",
            style={
                "backgroundColor": "lightgrey",
                "width": "1000px",
            },
        ),
    ],
    id="container",
    style={"width": "600px"},
)


@app.callback(
    Output("input", "save"),
    Input("save-button", "n_clicks"),
)
def save_signature_value(n_clicks):
    if n_clicks is not None and n_clicks > 0:
        return True
    return False


@app.callback(
    Output("input", "value"),
    [
        Input("clear-button", "n_clicks"),
    ],
)
def submit_signature_value(clicks):
    if clicks is not None and clicks > 0:
        return ""


@app.callback(
    Output("output", "children"),
    [Input("input", "value"), Input("store-button", "n_clicks")],
)
def update_output(value, clicks):
    context = ctx.triggered_id if not None else "no trigger"
    if clicks is not None and clicks > 0 and context == "store-button":
        return value


if __name__ == "__main__":
    app.run_server(debug=True)
