# st.write PRACTICE

import time

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# DEPLOY A TITTLE
"""
# THIS IS A PRACTICE FOR STREAMLIT
"""

# TYPOGRAPHY
"""
CHANGE _typography_ with _underscores_
"""

# DEPLOY A MESSAGE
st.write("Hello, *World* :sunglasses:")


# DEPLOY A TABLE
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4, "8"],
            "second column": [10, 20, 30, 40, "0"],
            "third column": [2, 4, 6, 8, "0"],
            "fourth column": [2, 4, 6, 8, "0"],
        }
    )
)

# MESSAGES WITH DATAFRAMES
st.write(
    "Below is a DataFrame:",
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4, 8],
            "second column": [10, 20, 30, 40, 0],
            "third column": [2, 4, 6, 8, "0"],
        }
    ),
    "Above is a dataframe.",
)

# DEPLOY CHART OBJECTS/GRAPHICS
# df(pd.Dataframe(np.random.rand(rows,columns), columns=[column1,column2,column3,...]))
# np.random.rand(rows,columns) generates a NumPy array with n rows and m columns of random numbers between 0 and 1.
df = pd.DataFrame(np.random.rand(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df)
    .mark_point()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(c)

# IDK WHAT THIS IS FOR (st.write_stream)
LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""


def stream_data():
    for word in LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.rand(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("Stream data"):
    st.write_stream(stream_data)
    st.write_stream(stream_data)


# USE OF MAGIC
# you dont have to st.write for the info to display
df = pd.DataFrame({"col1": ["1", "2", "3"]})
df


#######################################################

# USE OF TITLES
st.title("NEW _LEARNING STREAMLIT_ SECTION:  :red[TEXT ELEMENTS]")


# USE OF HEADERS
st.header("This is a header with a divider", divider="red")
st.header(
    "These headers have rotating dividers", divider=True
)  # rotating dividers means dividers would be changing its color
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)


# USE OF SUB HEADER
# subheader means the typography is smaller than normal header
st.subheader("This is a subheader with a divider", divider="gray")
st.subheader("These subheader have rotating dividers", divider=True)
st.subheader("One", divider=True)
st.subheader("Two", divider=True)
st.subheader("Three", divider=True)
st.subheader("Four", divider=True)


# USE OF MARKDOWNS
st.markdown(
    "-> >="
)  # markdown can be used to transform some symbols into its formal way


st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown(
    """
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text."""
)
st.markdown(
    "Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:"
)

multi = """If you end a line with two spaces,
a soft return is used for the next line.  

Two (or more) newline characters in a row will result in a hard return.
"""
st.markdown(multi)


# USE OF BADGES
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

# for multiple badges
st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

# equivalence between .markdown and .badge
st.markdown(":blue-badge[:material/star: Home]")
st.badge("Home", icon=":material/star:", color="blue")


# USE OF CAPTION
st.caption("THIS IS NOT A TEXT!, THIS PART IS BEING USE FOR CAPTION")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")


# USE OF CODE
code = """def hello():
    print("Hello, Streamlit!")"""

st.code(code, language="python")

# cant print this the way it is with .write
code2 = """Is it a crown or boat?
                        ii
                      iiiiii
WWw                 .iiiiiiii.                ...:
 WWWWWWw          .iiiiiiiiiiii.         ........
  WWWWWWWWWWw    iiiiiiiiiiiiiiii    ...........
   WWWWWWWWWWWWWWwiiiiiiiiiiiiiiiii............
    WWWWWWWWWWWWWWWWWWwiiiiiiiiiiiiii.........
     WWWWWWWWWWWWWWWWWWWWWWwiiiiiiiiii.......
      WWWWWWWWWWWWWWWWWWWWWWWWWWwiiiiiii....
       WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWwiiii.
          -MMMWWWWWWWWWWWWWWWWWWWWWWMMM-
"""
st.code(code2, language=None)


# USE OF DIVIDER
st.subheader("TEXTO1", divider=False)
st.divider()  # is the same as writing "---"
"---"
st.subheader("TEXTO2")


# USE OF ECHO
def get_user_name():
    return "John"


# ------------------------------------------------
# Want people to see this part of the code...
with st.echo():

    def get_punctuation():
        return "!!!"

    greeting = "Hi there, "
    user_name = get_user_name()
    punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------
st.write("Done!")


# USE OF LATEX
st.latex(
    """
    cos^{2}(\phi) = sen^{2}(\phi)
    """
)
# just a few commands from Latex are supported,
# consult on https://katex.org/docs/supported.html


# USE OF HELP
# st.help(np.random.rand(0, 9))
# st.help(pd.array)
# st.help(pd.DataFrame)

st.title("NEW LEARNING _STREAMLIT_ SECTION: :red[DATA ELEMENTS] ")

# USE OF DATAFRAME
"""
df = pd.DataFrame(np.random.rand(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  # is the same as writing st.write(df)
#st.write(df)}
"""

df = pd.DataFrame(np.random.rand(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))
st.write(df.style.highlight_max(axis=0))

# USE OF DATA_EDITOR
df2 = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(df2)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


st.title("NEW _LEARNING_ STREAMLIT SECTION: :red[CHART ELEMENTS]")

# USE OF AREA_CHART
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.write(chart_data)
st.area_chart(chart_data)


# USE OF BAR_CHART
# example 1
bar_chart = pd.DataFrame(np.random.randn(3, 3), columns=["a", "b", "c"])

st.bar_chart(bar_chart)


st.title("NEW LEARNING _STREAMLIT_ SECTION: :red[INPUT WIDGETS]")

# USE OF BUTTON
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")


# USE OF DOWNLOAD_BUTTON
@st.cache_data
def get_data():
    df = pd.DataFrame(
        np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
    )
    return df


@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")


df = get_data()
csv = convert_for_download(df)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
)

""""
st.title("NEW LEARNING _STREAMLIT_ SECTION: :red[MEDIA ELEMENTS]")

# USE OF IMAGE
st.image("HP.png", caption="JUST A BIG HAPPY FACE :)")

# USE OF AUDIO
st.audio("cat-purr.mp3", format="mp3", loop=False)


st.title("NEW LEARNING _STREAMLIT_ SECTION: :red[LAYOUTS & CONTAINERS]")

# USE OF COLUMNS
# example 1
col1, col2, col3, col4, col5, col6 = st.columns(6)


with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")


with col5:
    st.write(":green[CAT SOUNDS]")
    st.audio("cat-purr.mp3", format="mp3")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

with col4:
    st.write("NO IMAGES HERE JUST TEXT")


# example 2
col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)


# USE OF CONTAINER
with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")
"""