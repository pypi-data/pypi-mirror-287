import streamlit as st
from streamlit_tree_independent_components import tree_independent_components

st.subheader("Component with input args")

treeItems =  {
  "id": "0",
  "name": "Parent",
  "icon":"folder",
  'disable':False,
  "children": [
    {
      "id": "1",
      "name": "Child - 1",
      "icon":"folder",
    },
    {
      "id": "2",
      "name": "Child - 2",
      "icon":"document",
      'disable':False,
      "children": [
        {
          "id": "3",
          "name": "Child - 3",
          "icon":"document",
          "children": [
            {
              "id": "4",
              "name": "Child - 4",
              "icon":"settings",
            },
            {
              "id": "5",
              "name": "Child - 5",
              "icon":"folder",
              "children": [
                {
                  "id": "6",
                  "name": "Child - 6",
                  "icon":"settings",
                  "disable":False
                },
              ],
            },
          ],
        },
      ],
    },
    {
      "id": "7",
      "name": "Child - 7",
      "icon":"folder",
      'disable': True,
      "children": [
        {
          "id": "8",
          "name": "Child - 8",
          "icon":"folder",
          'disable': False
        },
      ],
    },
  ],
}
checkItems = ["0","1","2","3","4","5","6","7"]

result = tree_independent_components(treeItems, checkItems, expandItems=checkItems)

st.write(result)
