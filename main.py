import openai

import os
from dotenv import load_dotenv
load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = st.secrets["OPENAI_API_KEY"]

def check_if_not_null(query):
    if(query == ""):
        return 0
    else:
        return 1

def pass_prompt_to_ai(prompt,para):
    response = openai.Completion.create(
        engine = "davinci-codex",
        max_tokens = 1024,
        prompt = prompt,
        temperature = para[0], # Risk taking ability - 0
        top_p = para[1], # Influncing sampling - 1.0
        frequency_penalty = para[2], # Penalties for repeated tokens - 0.0
        presence_penalty = para[3], # Penalties for new words - 0.0
        #stop = ['#'] # when to stop generating
    )
    return response.choices[0].text
    #return response.choices

def fix_error_func(query):
    if(check_if_not_null(query)):
        prompt_fn = "\nFix the syntax errors in the above code\n"
        prompt = query + prompt_fn
        print(prompt)
        return pass_prompt_to_ai(prompt,[0,1.0,0.2,0.0])
    else:
        return "No Input"

def opt_code_func(query):
    if(check_if_not_null(query)):
        prompt_fn = "\nOptimize the above code and mention the optimizations"
        prompt =  query + prompt_fn
        print(prompt)
        return pass_prompt_to_ai(prompt,[0,1.0,0.2,0.0])
    else:
        return "No Input"

def promt_to_code_func(query):
    if(check_if_not_null(query)):
        prompt_fn = "Write a code for "
        prompt = prompt_fn + query
        print(prompt)
        return pass_prompt_to_ai(prompt,[0,1.0,0.2,0.0])
    else:
        return "No Input"

def explain_code_func(query):
    if(check_if_not_null(query)):
        prompt_fn = "\nExplain the logic of the above code\n"
        prompt = query + prompt_fn
        print(prompt)
        return pass_prompt_to_ai(prompt,[0,1.0,0.2,0.0])
    else:
        return "No Input"

def convert_lang_func(query,to_lang):
    if(check_if_not_null(query)):
        prompt_fn = f"Convert the following code to {to_lang}\n"
        prompt = prompt_fn + query
        print(prompt)
        return pass_prompt_to_ai(prompt,[0,1.0,0.2,0.0])
    else:
        return "No Input"

# ---------------------------------------------------------------------------------------------

import streamlit as st
from streamlit_ace import st_ace

st.set_page_config(page_icon=":computer:", layout = "wide")

# #238636
st.write("<div style='text-align: center'><h1>Code <em style='text-align: center; color: #238636;'>PRO</em></h1></div>", unsafe_allow_html=True)

LANGUAGES = [
    "abap", "abc", "actionscript", "ada", "alda", "apache_conf", "apex", "applescript", "aql", 
    "asciidoc", "asl", "assembly_x86", "autohotkey", "batchfile", "c9search", "c_cpp", "cirru", 
    "clojure", "cobol", "coffee", "coldfusion", "crystal", "csharp", "csound_document", "csound_orchestra", 
    "csound_score", "csp", "css", "curly", "d", "dart", "diff", "django", "dockerfile", "dot", "drools", 
    "edifact", "eiffel", "ejs", "elixir", "elm", "erlang", "forth", "fortran", "fsharp", "fsl", "ftl", 
    "gcode", "gherkin", "gitignore", "glsl", "gobstones", "golang", "graphqlschema", "groovy", "haml", 
    "handlebars", "haskell", "haskell_cabal", "haxe", "hjson", "html", "html_elixir", "html_ruby", "ini", 
    "io", "jack", "jade", "java", "javascript", "json", "json5", "jsoniq", "jsp", "jssm", "jsx", "julia", 
    "kotlin", "latex", "less", "liquid", "lisp", "livescript", "logiql", "logtalk", "lsl", "lua", "luapage", 
    "lucene", "makefile", "markdown", "mask", "matlab", "maze", "mediawiki", "mel", "mixal", "mushcode", 
    "mysql", "nginx", "nim", "nix", "nsis", "nunjucks", "objectivec", "ocaml", "pascal", "perl", "perl6", 
    "pgsql", "php", "php_laravel_blade", "pig", "plain_text", "powershell", "praat", "prisma", "prolog", 
    "properties", "protobuf", "puppet", "python", "qml", "r", "razor", "rdoc", "red", "redshift", "rhtml", 
    "rst", "ruby", "rust", "sass", "scad", "scala", "scheme", "scss", "sh", "sjs", "slim", "smarty", 
    "snippets", "soy_template", "space", "sparql", "sql", "sqlserver", "stylus", "svg", "swift", "tcl", 
    "terraform", "tex", "text", "textile", "toml", "tsx", "turtle", "twig", "typescript", "vala", "vbscript", 
    "velocity", "verilog", "vhdl", "visualforce", "wollok", "xml", "xquery", "yaml"
    ]

THEMES = [
    "ambiance", "chaos", "chrome", "clouds", "clouds_midnight", "cobalt", "crimson_editor", "dawn",
    "dracula", "dreamweaver", "eclipse", "github", "gob", "gruvbox", "idle_fingers", "iplastic",
    "katzenmilch", "kr_theme", "kuroir", "merbivore", "merbivore_soft", "mono_industrial", "monokai",
    "nord_dark", "pastel_on_dark", "solarized_dark", "solarized_light", "sqlserver", "terminal",
    "textmate", "tomorrow", "tomorrow_night", "tomorrow_night_blue", "tomorrow_night_bright",
    "tomorrow_night_eighties", "twilight", "vibrant_ink", "xcode"
    ]

first,second = st.columns((1,1))

def update(pro_output):
    with second:
        #st.markdown("## Output")
        st.code(pro_output, language = 'text')

def app():
    answer = ""
    
    with first:
        st.markdown("## Input")
        user_input = st_ace(
            value=answer,
            placeholder="Write your code or prompt here ...",
            height=800,
            language = st.sidebar.selectbox('Select Input Language', LANGUAGES, index=121),
            theme = st.sidebar.selectbox('Select Editor Theme', THEMES, index=5))

    with second:
        st.markdown("## Output")

    st.sidebar.title("Options")
    
    fix_error_button = st.sidebar.button('Fix Errors')
    Optimise_code_button = st.sidebar.button('Optimise Code')
    Prompt_to_code_button = st.sidebar.button('Prompt to Code')
    Explain_code_button = st.sidebar.button('Explain Code')

    to_lang = st.sidebar.selectbox('Convert to', LANGUAGES, index=68)
    Convert_lang_button = st.sidebar.button('Convert Code')

    # Define what happens when the button is clicked
    if fix_error_button:
        st.write('Button clicked!')
        answer = fix_error_func(user_input)
        update(answer)

    if Optimise_code_button:
        st.write('Button clicked!')
        answer = opt_code_func(user_input)
        update(answer)

    if Prompt_to_code_button:
        st.write('Button clicked!')
        answer = promt_to_code_func(user_input)
        update(answer)

    if Explain_code_button:
        st.write('Button clicked!')
        answer = explain_code_func(user_input)
        print(answer)
        update(answer)

    if Convert_lang_button:
        st.write('Button clicked!')
        answer = convert_lang_func(user_input,to_lang)
        update(answer)

def main():
    app()

if __name__ == "__main__":
    main()
