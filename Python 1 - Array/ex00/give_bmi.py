def give_bmi(height: list[int | float],
             weight: list[int | float]
             ) -> list[int | float]:
    """
    take 2 lists of integers or foats in input and calculte a list
    of BMI values.
    """
    try:
        assert len(height) == len(
            weight
        ), "weight and size lists need to be the same lenght."
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)
                              ) or not isinstance(w, (int, float)):
                raise ValueError("lists must only contain integers or floats")
            else:
                if h < 0 or w < 0:
                    raise ValueError("lists must only contain positive values")
    except Exception as e:
        print(f"An error occured: {e}")
        exit(1)
    bmi_values = []
    for h, w in zip(height, weight):
        bmi = w / (h**2)
        bmi_values.append(bmi)
    return bmi_values


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    accepts a list of integers or floats and an integer representing
    a limit as parameters and define if BMI is above the limit or not
    """
    try:
        if not isinstance(limit, (int, float)):
            raise ValueError("Limit must only be amd integers or a float")
    except Exception as e:
        print(f"An error occured: {e}")
        exit(1)
    result = []
    for value in bmi:
        result.append(value > limit)
    return result


def main():
    return


if __name__ == "__main__":
    main()
