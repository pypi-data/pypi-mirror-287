from setuptools import setup, find_packages

setup(
    name='simple_rocket_chat_sender',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv'
    ],
    description='Send Rocket Chat messages to your server',
    author='Gerardo Mathus',
    author_email='gerardo@hybridge.education',
    url='https://github.com/hybridgeeducation/simple-rocket-chat-sender',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
