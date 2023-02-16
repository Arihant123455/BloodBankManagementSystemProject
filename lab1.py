{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPTcySODZ/bp1g4fG9oayrG",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Arihant123455/BloodBankManagementSystemProject/blob/main/lab1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mErIbw4l0Ikg"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# New Section"
      ],
      "metadata": {
        "id": "FDz1RtR10MGV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Examples of list comprehension in python\n"
      ],
      "metadata": {
        "id": "LfgZpONA0OR2"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "print square of natural number 1 to 10\n",
        "\n"
      ],
      "metadata": {
        "id": "3IahomJM0UTl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1, 11):\n",
        "    print(i*i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nmQuCaIa0a0e",
        "outputId": "d7aa69a9-3372-4d49-cca7-a23bc3939562"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "4\n",
            "9\n",
            "16\n",
            "25\n",
            "36\n",
            "49\n",
            "64\n",
            "81\n",
            "100\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "count number of 6 between 1 to 1000."
      ],
      "metadata": {
        "id": "90lEvMyS1HL2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "count = 0\n",
        "for i in range(1, 1001):\n",
        "    count += str(i).count('6')\n",
        "print(count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y7HBMAf61PF2",
        "outputId": "2b077418-5e1b-440e-8779-4bb6205983b2"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "300\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "count number of spaces in string\n"
      ],
      "metadata": {
        "id": "sRIrCZll1cx2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "my_string = \"This is a string with some spaces\"\n",
        "space_count = my_string.count(\" \")\n",
        "print(\"Number of spaces in the string:\", space_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t1oOditB1i5P",
        "outputId": "510f2b48-acdf-45ed-e418-b97496b6b1b2"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of spaces in the string: 6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "write table of 5."
      ],
      "metadata": {
        "id": "TkSiOPGt1101"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1, 11):\n",
        "    print(\"5 x\", i, \"=\", 5*i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yX2WRIi819FN",
        "outputId": "30ce0d5a-d9d5-42eb-fef2-05dfbe23b07e"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 x 1 = 5\n",
            "5 x 2 = 10\n",
            "5 x 3 = 15\n",
            "5 x 4 = 20\n",
            "5 x 5 = 25\n",
            "5 x 6 = 30\n",
            "5 x 7 = 35\n",
            "5 x 8 = 40\n",
            "5 x 9 = 45\n",
            "5 x 10 = 50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "find number between 1 to 100 which is divisible by 2 and 5."
      ],
      "metadata": {
        "id": "8k2tcIS_2IEV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1, 101):\n",
        "    if i % 10 == 0:\n",
        "        print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tcPzA4YM2Rpt",
        "outputId": "6ff98076-43a5-4323-8da6-6637396cba66"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n",
            "20\n",
            "30\n",
            "40\n",
            "50\n",
            "60\n",
            "70\n",
            "80\n",
            "90\n",
            "100\n"
          ]
        }
      ]
    }
  ]
}