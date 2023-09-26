from flask import Flask, render_template , jsonify , request
import os,json

def link_generator(query):
    return "https://go.drugbank.com/unearth/q?query="+query+"&button=&searcher=drugs"

def run_scrapy(link,query):
    command=f'scrapy crawl para -a start_urls="{link}" -O ./db/{query}.json'
    curr_dir =os.getcwd()
    os.chdir("./try_drugbank/")
    a=os.system(command)
    print("Response of os.system(cmd) : "+str(a))
    with open(f"./db/{query}.json") as f:
        res= json.load(f)
    # os.remove(f"{query}.json")
    os.chdir(curr_dir)
    return res

def check_file_exists(query):
    curr_dir =os.getcwd()
    os.chdir("try_drugbank/db/")
    print(os.path.isfile(f"{query}.json"))
    res= os.path.isfile(f"{query}.json")
    os.chdir(curr_dir)
    return res

def get_file_data(query):
    curr_dir =os.getcwd()
    os.chdir("try_drugbank/db/")
    with open(f"{query}.json") as f:
        res= json.load(f)
    # os.remove(f"{query}.json")
    os.chdir(curr_dir)
    return res

app = Flask(__name__)

@app.route('/api/<query>')
def getinfo(query):
    query=query.lower()
    if (check_file_exists(query)):
        return get_file_data(query)[0]
    else:
        link= link_generator(query)
        info = run_scrapy(link,query)
        return info[0]

@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method =="POST":
        query=request.form['query'].lower()
        if (check_file_exists(query)):
            return render_template('show_data.html',info=get_file_data(query)[0])
        else:
            link= link_generator(query)
            info = run_scrapy(link,query)
            return render_template('show_data.html',info=info[0])
    else:
        return render_template('welcome.html')

        


