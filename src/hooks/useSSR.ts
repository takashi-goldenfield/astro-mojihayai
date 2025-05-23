function useSSR() {
  const isDOM = Boolean(
    typeof window !== "undefined" &&
      window.document &&
      window.document.documentElement,
  );

  return {
    isBrowser: isDOM,
    isServer: !isDOM,
  };
}

export default useSSR;
