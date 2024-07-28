import setuptools 
  
with open("README.md", "r") as fh: 
    description = fh.read() 
  
setuptools.setup( 
    name="voicecord", 
    version="2.1.0", 
    author="Peter Till", 
    author_email="ptertill@gmail.com", 
    packages=["voicecord"], 
    description="A simple yet powerful voice recording package for Discord", 
    long_description=description, 
    long_description_content_type="text/markdown", 
    url="https://github.com/petertill/voicecord", 
    license='MIT', 
    python_requires='>=3.8', 
    install_requires=["pynacl"]
) 