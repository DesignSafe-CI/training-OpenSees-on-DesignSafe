pip install jupyter-book
pip install OpenSeesPy

cd ~/MyData/_ToCommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe

jupyter-book clean . --all; python generate_md_toc.py ; jupyter-book build .





