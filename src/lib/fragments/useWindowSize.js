import React from "react";
// https://stackoverflow.com/a/63010184
function debounce(fn, ms) {
  let timer;
  return _ => {
    clearTimeout(timer);
    timer = setTimeout(_ => {
      timer = null;
      fn.apply(this, arguments);
    }, ms);
  };
}

const useWindowSize = () => {
  const [size, setSize] = React.useState([0, 0, false]);
  React.useLayoutEffect(() => {
    let timeout;
    clearTimeout(timeout);
    function updateSize() {
      clearTimeout(timeout);
      setSize([window.innerWidth, window.innerHeight, true]);
      timeout = setTimeout(() => {
        setSize([window.innerWidth, window.innerHeight, false]);
      }, 800);
    }
    const debouncedResizeHandler = debounce(() => updateSize())
    window.addEventListener('resize', debouncedResizeHandler);
    setSize([window.innerWidth, window.innerHeight, false]);
    return () => window.removeEventListener('resize', debouncedResizeHandler);
  }, []);
  return size;
}

export { useWindowSize }