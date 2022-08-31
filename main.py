from Traffic_sign_classification.predict import traffic


if __name__ == '__main__':   #Program entry

    traffic = traffic("Traffic_sign_classification/inputImage.jpg")
    result = traffic.trafficsign()
    print(result)

