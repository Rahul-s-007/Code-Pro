import openai

# import os
# from dotenv import load_dotenv
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

import streamlit as st
from streamlit_ace import st_ace

openai.api_key = st.secrets["OPENAI_API_KEY"]

def check_if_not_null(query):
    if(query == ""):
        return 0
    else:
        return 1

# ---------------------------------------------------------------------------------------------
# Done
def pass_prompt_to_ai_fix_error_func(prompt):
    response = openai.Completion.create(
        engine = "davinci-codex",
        max_tokens = 512,
        prompt = prompt,
        temperature = 0, # Risk taking ability - 0
        top_p = 1.0, # Influncing sampling - 1.0
        frequency_penalty = 0.0, # Penalties for repeated tokens - 0.0
        presence_penalty = 0.0, # Penalties for new words - 0.0
        stop = ["#"] # when to stop generating
    )
    return response.choices[0].text

def fix_error_func(query,inp_lang):
    if(check_if_not_null(query)):
        prompt_fn = f"##### Fix bugs in the below code\n \n### Buggy {inp_lang}\n{query}\n \n### Fixed {inp_lang}"
        prompt = prompt_fn
        print(prompt)
        return pass_prompt_to_ai_fix_error_func(prompt)
    else:
        return "No Input"

# ---------------------------------------------------------------------------------------------
# Done
def pass_prompt_to_ai_opt_code_func(prompt):
    response = openai.Completion.create(
        engine = "davinci-codex",
        max_tokens = 512,
        prompt = prompt,
        temperature = 0, # Risk taking ability - 0
        top_p = 1.0, # Influncing sampling - 1.0
        frequency_penalty = 0.0, # Penalties for repeated tokens - 0.0
        presence_penalty = 0.0, # Penalties for new words - 0.0
        stop = ["#"] # when to stop generating
    )
    return response.choices[0].text

def opt_code_func(query,inp_lang):
    if(check_if_not_null(query)):
        prompt_fn = f"##### Improve the time complexity and memory usage for the below code\n   \n### Given {inp_lang} code\n{query}\n   \n### Improved code"
        prompt = prompt_fn
        print(prompt)
        return pass_prompt_to_ai_opt_code_func(prompt)
    else:
        return "No Input"

# ---------------------------------------------------------------------------------------------
# Done
def pass_prompt_to_ai_promt_to_code_func(prompt):
    response = openai.Completion.create(
        engine = "davinci-codex",
        max_tokens = 512,
        prompt = prompt,
        temperature = 0, # Risk taking ability - 0
        top_p = 1.0, # Influncing sampling - 1.0
        frequency_penalty = 0.0, # Penalties for repeated tokens - 0.0
        presence_penalty = 0.0, # Penalties for new words - 0.0
        stop = ["#"] # when to stop generating
    )
    return response.choices[0].text

def promt_to_code_func(query):
    if(check_if_not_null(query)):
        prompt_fn = f"##### Write code for the below prompt\n   \n### Given Prompt\n{query}\n   \n### Code for prompt"
        prompt = prompt_fn
        print(prompt)
        return pass_prompt_to_ai_promt_to_code_func(prompt)
    else:
        return "No Input"

# ---------------------------------------------------------------------------------------------
# Done
def pass_prompt_to_ai_explain_code_func(prompt):
    response = openai.Completion.create(
        engine = "davinci-codex",
        max_tokens = 512,
        prompt = prompt,
        temperature = 0, # Risk taking ability - 0
        top_p = 1.0, # Influncing sampling - 1.0
        frequency_penalty = 0.0, # Penalties for repeated tokens - 0.0
        presence_penalty = 0.0, # Penalties for new words - 0.0
        stop = ["\"\"\""] # when to stop generating
    )
    return response.choices[0].text

def explain_code_func(query):
    if(check_if_not_null(query)):
        prompt_fn = "\n\"\"\"\nHere's what the above code is doing:\n"
        prompt = query + prompt_fn
        print(prompt)
        return pass_prompt_to_ai_explain_code_func(prompt)
    else:
        return "No Input"
    

# ---------------------------------------------------------------------------------------------
# Done
def pass_prompt_to_ai_convert_lang_func(prompt):
    response = openai.Completion.create(
        engine = "davinci-codex",
        max_tokens = 256,
        prompt = prompt,
        temperature = 0, # Risk taking ability - 0
        top_p = 1.0, # Influncing sampling - 1.0
        frequency_penalty = 0, # Penalties for repeated tokens - 0.0
        presence_penalty = 0, # Penalties for new words - 0.0
        stop = ["#"] # when to stop generating
    )
    return response.choices[0].text

def convert_lang_func(query,inp_lang,to_lang):
    if(check_if_not_null(query)):
        prompt_fn = f"##### Translate this code from {inp_lang} into {to_lang}\n### {inp_lang}\n{query}\n### {to_lang}"
        prompt = prompt_fn
        print(prompt)
        return pass_prompt_to_ai_convert_lang_func(prompt)
    else:
        return "No Input"

# ---------------------------------------------------------------------------------------------

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
    
    inp_language = st.sidebar.selectbox('Select Input Language', LANGUAGES, index=121)

    with first:
        st.markdown("## Input:")
        user_input = st_ace(
            value=answer,
            placeholder="Write your code or prompt here ...",
            height=600,
            language = inp_language,
            theme = st.sidebar.selectbox('Select Editor Theme', THEMES, index=5))

    with second:
        st.markdown("## Output:")

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
        answer = fix_error_func(user_input,inp_language)
        update(answer)

    if Optimise_code_button:
        st.write('Button clicked!')
        answer = opt_code_func(user_input,inp_language)
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
        answer = convert_lang_func(user_input,inp_language,to_lang)
        update(answer)

def main():
    app()

if __name__ == "__main__":
    main()
