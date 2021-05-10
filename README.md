# Object Skeletonization: Comparing State of the Art algorithms

### Project was done as part of CV course in the Winter 2021 semester of IIITD under the guidance of Prof. Koteswar Rao Jerripothula by: 
* Daksh Thapar [daksh18137@iiitd.ac.in]
* Himanshu Raj [himanshu18038@iiitd.ac.in]
* Naman Tyagi [naman18055@iiitd.ac.in]
* Pankil Kalra [pankil18061@iiitd.ac.in]

## Abstract
Given an image, we identify and highlight the topological skeleton region of object(s) present in the image using thinning techniques based on Zhang Suen Algorithm, Guo Hall Algorithm, start of the art techniques like KMM Thinning Algorithm, K3M Thinning Algorithm and Modified K3M Thinning Algorithm. 
The objective is to then qualitatively and quantitatively compare their performances based on multiple factors like types of image geometry, Thinning Rate (TR), Thinning Speed (TS), object points, preservation of right angles, topology and presence of 1-pixel width.


## Directory Structure
* [zs.py](zs.py)  - Zhang Suen Algorithm
* [gh.py](gh.py)  - Guo Hall Algorithm
* [kmm.py](kmm.py)  - KMM Algorithm
* [k3m.py](k3m.py)  - K3M Algorithm
* [mod_k3m.py](mod_k3m.py)  - Modified K3M Algorithm
* [Images](Images/) - Inpute Images
* [Output](Output/) - Output Images

## Links to the papers of the different algorithms:
* Zhang Suen [[Link]](http://agcggs680.pbworks.com/f/Zhan-Suen_algorithm.pdf)
* Guo Hall [[Link]](https://dl.acm.org/doi/abs/10.1145/62065.62074)
* KMM [[Link]](https://www.researchgate.net/publication/220913832_Implementation_and_Advanced_Results_on_the_Non-interrupted_Skeletonization_Algorithm)
* K3M [[Link]](https://www.researchgate.net/publication/220273912_K3M_A_universal_algorithm_for_image_skeletonization_and_a_review_of_thinning_techniques)
* Modified K3M [[Link]](https://www.researchgate.net/publication/304997206_A_modified_K3M_thinning_algorithm)



