export function middleEllipsis(
  str = "",
  maxLength = 15,
  charsStart = 7,
  charsEnd = 7
) {
  if (str.length > maxLength) {
    return `${str.slice(0, charsStart)}...${str.slice(str.length - charsEnd, str.length)}`;
  }
  return str;
}
