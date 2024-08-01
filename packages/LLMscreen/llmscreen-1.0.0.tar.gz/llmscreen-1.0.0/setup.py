from setuptools import setup, find_packages

setup(
    name='LLMscreen',
    version='1.0.0',
    description='A package for filtering abstracts using OpenAI models.',
    long_description= '''LLMscreen is a package that allows users to filter and process research abstracts 
                         based on given criteria using OpenAI's language models. It supports both simple 
                         and zeroshot approaches for inclusion criteria and provides detailed outputs 
                         including probabilities and perplexity scores.''',
    author='Jinquan Ye',
    author_email='jinquan.ye@duke.edu',
    url='https://github.com/yebarryallen/LLMscreen',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'openai'
        # Add any other dependencies here
    ],
    keywords=['abstract filtering', 'OpenAI', 'systematic reviews', 'research'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
