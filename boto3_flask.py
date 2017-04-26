import boto3
from flask import Flask
from flask import render_template

boto3.setup_default_session(profile_name='hgprod')
ec2 = boto3.resource('ec2')
elb_client = boto3.client('elb')

def get_instances():
    return ec2.instances.all()

def get_elbs():
    response = elb_client.describe_load_balancers()

    elbs = []
    for elb in response['LoadBalancerDescriptions']:
        instances = []
        elb_dict = dict({'Name': elb['LoadBalancerName'], 'DNSName': elb['DNSName'], 'Az': elb['AvailabilityZones']})
        if elb['Instances']:
            for intance in elb['Instances']:
                instances.append(intance['InstanceId'])
            elb_dict['instances'] = instances
            lb = [elb_dict]
        else:
            lb = [elb_dict]
        elbs.append(lb)
    return elbs

def print_elbs(elbs):
    for elb in elbs:
        print(elb.Name, elb.instances)


instances = get_instances()
elbs = get_elbs()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/instance")
@app.route("/instance/<instance_id>")
def instance_page(instance_id):
    instance_obj = ec2.Instance(instance_id)
    return render_template('instance.html', instance=instance_obj)

@app.route("/elb")
@app.route("/elb/<elb_name>")
def elb_page(elb_name):
    elb_obj = elb_client.describe_load_balancers(LoadBalancerNames=[elb_name])['LoadBalancerDescriptions'][0]
    return render_template('elb.html', elb=elb_obj)

@app.route("/instances")
def instances_page():
    return render_template('instances.html', instances=instances)

@app.route("/elbs")
def elbs_page():
    return render_template('elbs.html', elbs=elbs)

@app.route("/child")
def child():
    return render_template('child.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.debug = True
    app.run()
