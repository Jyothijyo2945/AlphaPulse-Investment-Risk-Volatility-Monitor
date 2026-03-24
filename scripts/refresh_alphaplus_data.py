{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1fdd9892-9454-40f9-9bcf-c1427eb44e76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Starting data refresh...\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[*********************100%***********************]  11 of 11 completed\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data refresh completed.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import yfinance as yf\n",
    "\n",
    "print(\"Starting data refresh...\")\n",
    "\n",
    "# download data\n",
    "tickers = [\"AAPL\",\"MSFT\",\"GOOGL\",\"META\",\"AMZN\",\"JPM\",\"BAC\",\"JNJ\",\"XOM\",\"TSLA\",\"^GSPC\"]\n",
    "\n",
    "data = yf.download(tickers,start=\"2018-01-01\",auto_adjust=True)\n",
    "\n",
    "prices = data[\"Close\"]\n",
    "\n",
    "# save clean prices\n",
    "prices.to_csv(\"01_clean_prices.csv\")\n",
    "\n",
    "# log returns\n",
    "log_returns = np.log(prices/prices.shift(1)).dropna()\n",
    "log_returns.to_csv(\"02_log_returns.csv\")\n",
    "\n",
    "print(\"Data refresh completed.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58c8a1c7-09b5-49d6-809f-0bfa8af14d45",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
