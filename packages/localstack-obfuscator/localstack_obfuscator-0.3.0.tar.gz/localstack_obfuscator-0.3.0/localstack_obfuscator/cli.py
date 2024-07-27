_A=False
import argparse,os,python_minifier,yaml
from localstack_obfuscator.custom_patches import patch
CONFIG_FILE_NAME='obfuscator.yml'
def root_code_dir():dir=os.path.dirname(os.path.realpath(__file__));return os.path.realpath(os.path.join(dir,''))
def mkdir(path):
	if not os.path.exists(path):os.makedirs(path)
def run(cmd):os.system(cmd)
def copy_target_code(src_dir,build_dir,target_dir_name,remove=None):
	F=target_dir_name;D=remove;C=build_dir;A=src_dir;print(f"Copying target code from {A} to {C} while excluding patterns: {D}");B=os.path.join(C,F);mkdir(B)
	if D:G='\\|'.join(f"^{A}$"for A in D);E=f'cp -R $(ls "{A}" | grep -v "{G}" | sed "s|^|{A}/|") "{B}/"'
	else:E=f"cp -r {A} {B}"
	print(f"Copying {A} to {B} with command: {E}");run(E);return os.path.join(C,F)
def apply_python_minifier_patches():
	'Idempotent operation that applies required patches to python-minifier';C=True;import ast as B;from python_minifier.transforms.remove_annotations import RemoveAnnotations as A
	def F(node):
		F='dataclasses';E=node;D='dataclass'
		if not isinstance(E.parent,B.ClassDef):return _A
		if len(E.parent.decorator_list)==0:return _A
		for A in E.parent.decorator_list:
			if isinstance(A,B.Name)and A.id==D:return C
			elif isinstance(A,B.Call)and isinstance(A.func,B.Name)and A.func.id==D:return C
			elif isinstance(A,B.Attribute)and A.attr==D and A.value.id==F:return C
			elif isinstance(A,B.Call)and isinstance(A.func,B.Attribute)and A.func.attr==D and A.func.value.id==F:return C
		return _A
	if not hasattr(A.visit_AnnAssign,'_ls_patched'):
		@patch(A.visit_AnnAssign)
		def D(fn,self,node):
			E='annotation';A=node
			if F(A):return A
			if isinstance(A,B.AnnAssign):
				D=getattr(A,E,None);C=fn(self,A);G=getattr(C,E,None)
				if isinstance(G,B.Constant)and isinstance(D,(B.Subscript,B.Name)):C.annotation=D
				return C
			return fn(self,A)
		A.visit_AnnAssign._ls_patched=C
def load_file(path):
	with open(path,'r')as A:return A.read()
def save_file(path,content):
	with open(path,'w')as A:return A.write(content)
def load_config(config_path):
	try:A=open(config_path,'r');return yaml.safe_load(A)
	except FileNotFoundError:print(f"No {CONFIG_FILE_NAME} file found in target directory");return{}
def obfuscate(src_dir,config_file):
	B=src_dir;B=os.path.realpath(B);A=load_config(config_file)
	if A.get('custom_patches',_A):apply_python_minifier_patches()
	F=os.path.join(B,A.get('build_dir','build'));G=A.get('target_dir',os.path.basename(B));H=A.get('minify',{});I=A.get('exclude',[]);J=A.get('remove',[]);E=copy_target_code(B,F,G,remove=J);print(f"Starting obfuscation in {E}...")
	for(K,N,L)in os.walk(E):
		for C in L:
			if C in I or not C.endswith('.py'):continue
			D=os.path.join(K,C);print(f"Obfuscating {D}");M=python_minifier.minify(load_file(D),**H);save_file(D,M)
	print('Done!')
def main():A=argparse.ArgumentParser(description='Obfuscate LocalStack proprietary code base');A.add_argument('src_dir',type=str,help='Source directory to obfuscate');A.add_argument('--config',type=str,default=CONFIG_FILE_NAME,help='Configuration file');B=A.parse_args();obfuscate(B.src_dir,B.config)
if __name__=='__main__':main()