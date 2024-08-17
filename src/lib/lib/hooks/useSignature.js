import React from "react"

export const useSignature(ref){
  const resizeCanvas = React.useCallback((signatureRef, signaturePadRef) => {
    const canvas = signatureRef.current
    const ratio = Math.max(window.devicePixelRatio || 1, 1);
    canvas.width = canvas.offsetWidth * ratio;
    canvas.height = canvas.offsetHeight * ratio;
    canvas.getContext("2d").scale(ratio, ratio);
    signaturePadRef.current.clear(); // otherwise isEmpty() might return incorrect value
  }, [])
  React.useEffect(() => {
    if (signatureRef !== null) {
      signaturePadRef.current = new SignaturePad(signatureRef.current)
      resizeCanvas(signatureRef, signaturePadRef)
    }
  }, [])
  return {
    signature
  }
}