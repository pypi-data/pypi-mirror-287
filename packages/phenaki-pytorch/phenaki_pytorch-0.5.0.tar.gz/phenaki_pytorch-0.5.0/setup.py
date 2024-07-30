from setuptools import setup, find_packages

setup(
  name = 'phenaki-pytorch',
  packages = find_packages(exclude=[]),
  version = '0.5.0',
  license='MIT',
  description = 'Phenaki - Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/phenaki-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformers',
    'attention mechanisms',
    'text-to-video'
  ],
  install_requires = [
    'accelerate',
    'beartype',
    'einops>=0.7',
    'ema-pytorch>=0.2.2',
    'opencv-python',
    'pillow',
    'numpy',
    'sentencepiece',
    'torch>=1.6',
    'torchtyping',
    'torchvision',
    'transformers>=4.20.1',
    'tqdm',
    'vector-quantize-pytorch>=1.11.8'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
