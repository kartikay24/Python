{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled2.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Sv5NSJ2nYR6p",
        "outputId": "fdea158b-de83-4ca3-9b2a-dd7390fb3514"
      },
      "source": [
        "people = int(input(\"How many people do you want to invite? \"))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "How many people do you want to invite? 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1gk7Gq14YeE9",
        "outputId": "d02978ac-af2a-47f4-9d0d-3f8b810e9894"
      },
      "source": [
        " #Making a dictionary of the cost based on different US cities\n",
        "print(\"The costs stated here are to be interpreted in Dollars.\")\n",
        "print(\"Costs consist of the ceremony along with the venue booking bill\")\n",
        "print(\"THIS CHART MAYBE SUBJECTIVE TO CHANGES BASED ON DIFFERENT SITUATIONS\")\n",
        "cost_table = {\n",
        "    'New York':2830,\n",
        "    'Las Vegas':4200,\n",
        "    'California':2702,\n",
        "    'Los Angeles':4750\n",
        "    }"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The costs stated here are to be interpreted in Dollars.\n",
            "Costs consist of the ceremony along with the venue booking bill\n",
            "THIS CHART MAYBE SUBJECTIVE TO CHANGES BASED ON DIFFERENT SITUATIONS\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ybLJhyt2YkRv"
      },
      "source": [
        "flight_table = {\n",
        "    'New York':283,\n",
        "    'Las Vegas':420,\n",
        "    'California':272,\n",
        "    'Los Angeles':475\n",
        "    }"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qCz_EvoIYqvW"
      },
      "source": [
        "def ceremony_cost(city):\n",
        "    return cost_table.get(city)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yGzKyO7DYtQJ"
      },
      "source": [
        "def hotel_cost(nights): \n",
        "  food_cost = 50\n",
        "  cost = (140 + food_cost) * nights  * people\n",
        "  \n",
        "  return cost"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PxL7WCWjYvqY"
      },
      "source": [
        "# Assuming it's a destination wedding, plane cost is a necessity\n",
        "#\n",
        "def plane_ride_cost(city):\n",
        "    return flight_table.get(city)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4WhUasULYyNJ"
      },
      "source": [
        "def rental_car_cost(days): \n",
        "    discount_3 = 40 * days * 0.2 \n",
        "    discount_7 = 40 * days * 0.5 \n",
        "    total_rent3 = 40 * days - discount_3\n",
        "    total_rent7 = 40 * days - discount_7\n",
        "    cost_day = 40 * days \n",
        "\n",
        "    if days >= 3:\n",
        "        return total_rent3\n",
        "    elif days >= 7:\n",
        "        return total_rent7\n",
        "    else: \n",
        "        return cost_day"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DUGoMM4AY1K7"
      },
      "source": [
        "def trip_cost(city, nights, car_days):\n",
        "    total = hotel_cost(nights) + plane_ride_cost(city) +\\\n",
        "            rental_car_cost(car_days) + flight_table(city)\n",
        "    return total"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lJawKMQhY3ar",
        "outputId": "50f75351-bec6-4510-fe20-bf4019af2831"
      },
      "source": [
        "city = None\n",
        "while True:\n",
        "    city = input(\"What's our destination?\\n\")\n",
        "    if city not in cost_table:\n",
        "        print (\"That's not a valid destination.\")\n",
        "    else:\n",
        "        break"
      ],
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "What's our destination?\n",
            "Las Vegas\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w3A6BbdkY6dk",
        "outputId": "a68f2632-6815-40ce-bbd2-2c1af478abba"
      },
      "source": [
        "hotel_nights = int(input(\"\\nHow many nights will you stay?\\n\"))\n",
        "car_days = int(input(\"How many days will you rent the car?\\n\"))   \n",
        "\n",
        "total_trip_cost = int(hotel_cost(hotel_nights))+\\\n",
        "                  int(plane_ride_cost(city))+\\\n",
        "                  int(rental_car_cost(car_days))+\\\n",
        "                  int(ceremony_cost(city))\n",
        "total_trip_cost = total_trip_cost + (0.28 * total_trip_cost)\n",
        "print (\"The total cost with the trip is\", total_trip_cost, \"dollars.\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "How many nights will you stay?\n",
            "3\n",
            "How many days will you rent the car?\n",
            "3\n",
            "The total cost with the trip is 7495.68 dollars.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ufb6rtmiY_cB",
        "outputId": "aee5abdf-320e-4aa4-971a-5052bdff8ed9"
      },
      "source": [
        "total_trip_cost_converted = (lambda x: x * 73.12)\n",
        "print (\"The total cost with the trip is\",format(total_trip_cost_converted(total_trip_cost),'.2f'), \"rupees.\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The total cost with the trip is 548084.12 rupees.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SbeVFN2BZF0e"
      },
      "source": [
        "#total_trip_taxed = total_trip_cost_converted + tax_calculator(total_trip_cost_converted)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eUUMSh1fZJcY"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}