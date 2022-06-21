let dollarUSLocale = Intl.NumberFormat('en-US');

export const displayNumber = (amount) => {
  return dollarUSLocale.format(amount);
}

export const displayMoney = (amount) => {
  return "$" + dollarUSLocale.format(amount);
}