# Signal Triangulation

This project aims to practice and create an algorithm to triangulate the location of an emitter by receiving different data and comparing the final results. The goal is to identify where the problem lies, whether it is in the model or in the data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. It´s best to use virtual environments to run this project.

### Prerequisites
This project requires the following dependencies:

- Python 3.x
- Matplotlib
- Numpy

### Creating a virtual environment
```
python -m venv venv
```

### Installing

First, you need to activate the virtual environment:
Windows Users:
```
venv\Scripts\activate
```
Linux Users:
```
source venv/bin/activate
```

Then, you need to install the dependencies:
```
pip install -r requirements.txt
```

### Running the code

You can run the code by executing the `plotagem.py` file:
Windows Users:
```
python main.py
```
Linux Users:
```
python3 main.py
```

## Algorithm

The algorithm used in this project is based on signal triangulation using the power of signal method. The location of the emitter is calculated by measuring power emmited by the emitter, and then calculating the distance between the emitter and the receivers. The distance between the emitter and the receivers is calculated using the following formula:
dk = 10^((P0 - Pk) / 10 * lk)

Where:

## Data

The data used in this project consists of the coordinates of the receivers and the power of the signals at each receiver. The data can be found in the `PDF` file.

## Results

The final results of the triangulation are plotted on a graph using matplotlib. The plot shows the location of the emitter and the receivers, with circles to represent the calculated location of the emmiter with the given data.

## Conclusions

The results of this project demonstrate the effectiveness of the method for triangulating the location of an emitter. The algorithm was able to accurately calculate the location of the emitter using the data provided in two ways, demonstraiting that the problem lies in the data in one case, and in the model in the other.

## Authors

- [Henrique Ribeiro Favaro] - Initial work

## Acknowledgments

- This project was developed as a degree work.