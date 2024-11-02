import React from 'react';
import PropTypes from 'prop-types';
import SignaturePad from 'signature_pad';
// output.css is the tailwind css file that is generated from the tailwind.config.js
// This file is generated using the command `npm run css` while in the dash_signature directory.
// Some classes conflict with the existing bootstrap classes. To avoid conflicts, the conflicting classes should be renamed.
// Conflicting classes in this file are currently just `border` which is instead used as `border-[1px]` to avoid conflicts.
import '../css/output.css';
import {CloseIcon} from '../fragments/CloseIcon.react';
import {classNames} from '../utils/classNames';
import {ChevronIcon} from '../fragments/ChevronIcon.react';
import {useWindowSize} from '../fragments/useWindowSize';
import {EditIcon} from '../fragments/EditIcon.React';
import {TrashIcon} from '../fragments/TrashIcon.react';
/**
 *
 * @param {string} dataUri
 * @returns {boolean} isValidImageDataUri
 *
 * Function to check if a data URI is a valid image.
 */

// Sean trying to add basic stuff...
// class Signature2 extends Component {
//     constructor(props) {
//         super(props);
//         this.state = {
//             value: 'default',
//         };
//     }
// }

function isValidImageDataUri(dataUri) {
    // Regular expression to match a data URI for an image
    // const regex = /^data:image\/(svg\+xml);base64,[a-zA-Z0-9+/=]+$/;
    const regex = /^data:image\/(png|jpeg|svg\+xml);base64,[a-zA-Z0-9+/=]+$/;

    // Check if the data URI matches the pattern
    if (!regex.test(dataUri)) {
        return false;
    }
    // Try to decode the base64 part and check if it's a valid image
    try {
        const img = new Image();
        img.src = dataUri;

        // Check if the image loads without errors
        img.onload = function () {
            return true;
        };

        img.onerror = function () {
            return false;
        };
    } catch (error) {
        return false;
    }

    return true;
}
/**
 * Scale Data From:
 * Function outside react scope to prevent re-creation of the function on every render.
 */
function scaleDataFrom(data, canvas, height, width) {
    if (height === null || width === null) return data;
    if (data && Array.isArray(data) && canvas) {
        const scaleX = canvas.width / width;
        const scaleY = canvas.height / height;
        const scaledData = data.map((group) => {
            group.points = group.points.map((point) => {
                point.x *= scaleX;
                point.y *= scaleY;
                return point;
            });
            return group;
        });
        return scaledData;
    }
    return data;
}
/**
 * @typedef {Object} SignatureCanvasProps
 * @property {boolean} expanded - Whether the signature canvas is expanded or not.
 * @property {React.Dispatch<React.SetStateAction<boolean>>} setExpanded - Function to set the expanded state.
 * @property {boolean} isExpanded - Whether the signatureRef is pointing to the expandedSignatureCanvasRef or not.
 * @property {string} signatureData - Base64 data of the signature from SVG web URI.
 * @property {React.Dispatch<React.SetStateAction<string>>} setSignatureData - Setter of signatureData.
 * @property {React.Dispatch<React.SetStateAction<string>>} setSignatureValue - Setter of signatureValue.
 * @property {any[]} redos - List of SVG stroke data from signature pad JS.
 * @property {React.Dispatch<React.SetStateAction<any[]>>} setRedos - Setter of redos.
 * @property {string} value - Base64 data of the signature from SVG web URI.
 * @property {() => void} handleUndo - Function to handle undo action.
 * @property {() => void} handleRedo - Function to handle redo action.
 * @property {() => void} handleClear - Function to handle clear action.
 * @property {() => void} handleReset - Function to handle reset action.
 * @property {() => void} handleSave - Function to handle save action.
 * @property {number | null} oldHeight - Previous height of the canvas.
 * @property {number | null} oldWidth - Previous width of the canvas.
 * @property {React.Dispatch<React.SetStateAction<number | null>>} setOldHeight - Setter of oldHeight.
 * @property {React.Dispatch<React.SetStateAction<number | null>>} setOldWidth - Setter of oldWidth.
 */
/**
 * SignatureCanvas component.
 * This component renders a signature pad where users can draw their signature.
 * It supports expanding the canvas, undo, redo, and clear actions.
 * The signature data is stored in image/svg+xml uri format.
 *
 * @param {SignatureCanvasProps} props - The properties for the SignatureCanvas component.
 * @param {React.Ref} ref - The ref for the SignatureCanvas component.
 * @returns {JSX.Element} The rendered SignatureCanvas component.
 */
function SignatureCanvas(
    {
        expanded,
        setExpanded,
        isExpanded,
        signatureData,
        setSignatureData,
        setSignatureValue,
        redos,
        setRedos,
        value,
        handleUndo,
        handleRedo,
        handleClear,
        handleReset,
        handleSave,
        disabled,
        handleDisable,
        oldHeight,
        oldWidth,
        setOldHeight,
        setOldWidth,
    },
    ref
) {
    const signatureRef = React.useRef(null);
    const signaturePadRef = React.useRef(null);
    // Expose the following methods to the parent component.
    React.useImperativeHandle(ref, () => {
        return {
            // signature pad js reference functions. Refere to signature_pad.js documentation for more information.
            toDataURL: (type) => signaturePadRef.current.toDataURL(type),
            fromDataURL: (data) => signaturePadRef.current.fromDataURL(data),
            fromData: (data) => signaturePadRef.current.fromData(data),
            toData: () => signaturePadRef.current.toData(),
            clear: () => signaturePadRef.current.clear(),
            isEmpty: () => signaturePadRef.current.isEmpty(),
            off: () => signaturePadRef.current.off(),
            on: () => signaturePadRef.current.on(),
            // canvas element refs
            // the width/height of the canvas for the current reference element
            width: () => signatureRef.current.width,
            height: () => signatureRef.current.height,
            offsetWidth: () => signatureRef.current.offsetWidth,
            offsetHeight: () => signatureRef.current.offsetHeight,
            // get the context of the signature canvas
            getContext: (ctx) => signatureRef.current.getContext(ctx),
            // this function must be called in the parent component on render to resize the canvas
            resizeCanvas: (value) => resizeCanvas(value),

            // getter for the reference to the signature pad js class object
            get signaturePad() {
                return signaturePadRef.current;
            },
            // getter for the reference to the html canvas element
            get signatureCanvas() {
                return signatureRef.current;
            },
        };
    });

    /**
     * Scale Data:
     * This function will take some input data that is in the form of an array of stroke groups
     * and scale the data to the current canvas size.
     *
     * @param {*} data stroke data from signature pad js
     * @returns the input data scaled to the current canvas size
     */
    const scaleData = (data) => {
        if (oldHeight === null || oldWidth === null) return data;
        if (data && Array.isArray(data) && signatureRef.current) {
            const canvas = signatureRef.current;
            const scaleX = canvas.width / oldWidth;
            const scaleY = canvas.height / oldHeight;

            const scaledData = data.map((group) => {
                group.points = group.points.map((point) => {
                    point.x *= scaleX;
                    point.y *= scaleY;
                    return point;
                });
                return group;
            });
            return scaledData;
        }
    };

    /**
     * Resize Canvas:
     * This function depends on the isExpanded state to determine if the canvas should be resized.
     * If the canvas is being rendered on the expanded dialog, the canvas will be resized to match the dialog size
     * only when the dialog is expanded. Otherwise, the canvas will be resized to match the container size.
     *
     * We must check the isExpanded flag to prevent resizing the canvas twice as the dialog render
     * can possibly trigger a resize event twice when the dialog is expanded and is also being
     * shown as the normal canvas component.
     */
    const resizeCanvas = React.useCallback(
        (newValue) => {
            if (signatureRef.current && isExpanded) {
                const canvas = signatureRef.current;
                const oldWidth = canvas.width;
                const oldHeight = canvas.height;

                // Get the ratio of the display size to the actual size
                const ratio = Math.max(window.devicePixelRatio || 1, 1);

                // Set the canvas size to match its container's size
                canvas.width = canvas.offsetWidth * ratio;
                canvas.height = canvas.offsetHeight * ratio;

                // Scale the drawing context to match the canvas size
                const data = newValue ?? signaturePadRef.current.toData();
                const ctx = canvas.getContext('2d');
                ctx.scale(ratio, ratio);
                setOldHeight(canvas.height);
                setOldWidth(canvas.width);
                signaturePadRef.current.clear();
                if (data && Array.isArray(data)) {
                    const scaleX = canvas.width / oldWidth;
                    const scaleY = canvas.height / oldHeight;

                    const scaledData = data.map((group) => {
                        group.points = group.points.map((point) => {
                            point.x *= scaleX;
                            point.y *= scaleY;
                            return point;
                        });
                        return group;
                    });
                    signaturePadRef.current.fromData(scaledData);
                    setSignatureData(scaledData.length);
                    setSignatureValue(scaledData);
                } else {
                    if (isValidImageDataUri(newValue)) {
                        signaturePadRef.current.fromDataURL(newValue); //.then(() => {
                    }
                }
            }
        },
        [isExpanded]
    );
    const strokeEndEvent = React.useCallback(() => {
        if (ref.current) {
            setSignatureData(signaturePadRef.current.toData().length ?? 0);
            const data = signaturePadRef.current.toData();
            setSignatureValue(data);
            setRedos([]);
            handleSave()
        }
    }, [value]);
    const size = useWindowSize();
    React.useEffect(() => {
        if (!disabled && signaturePadRef.current) {
            resizeCanvas();
        }
        // resizeCanvas()
    }, [size, disabled]);
    React.useEffect(() => {
        // Add event listener for window resize
        signaturePadRef.current = new SignaturePad(signatureRef.current, {
            scale: -1,
        });
        // window.addEventListener('resize', resizeCanvas);
        signaturePadRef.current.addEventListener('endStroke', strokeEndEvent);
        if (isValidImageDataUri(value)) {
            resizeCanvas(value);
        } else {
            resizeCanvas(value);
        }
        return () => {
            signaturePadRef.current.removeEventListener(
                'endStroke',
                strokeEndEvent
            );
        };
    }, []);
    React.useEffect(() => {
        if (disabled && signaturePadRef.current) {
            signaturePadRef.current.off();
        } else if (!disabled && signaturePadRef.current) {
            signaturePadRef.current.on();
        }
    }, [disabled]);
    return (
        <div className="tw-flex tw-flex-col tw-relative tw-aspect-[5/2]">
            <div className="tw-absolute tw-z-20 tw-flex tw-bottom-0 tw-right-0 tw-p-1 tw-justify-end tw-gap-2">
                {disabled ? (
                    <button
                        type="button"
                        title="Edit"
                        className={classNames(
                            'active:tw-fill-blue-600 active:tw-bg-grey-400/50 hover:tw-bg-gray-300/50 tw-p-1 tw-rounded tw-z-20 tw-border-none tw-bg-transparent'
                        )}
                        onClick={() => handleDisable(false)}
                    >
                        <EditIcon className="tw-fill-inherit tw-p-[1px]" />
                    </button>
                ) : (
                    <>
                        <button
                            type="button"
                            title="Undo"
                            // disabled={redos.length === 0 || typeof value === 'string'}
                            className={classNames(
                                'active:tw-fill-blue-600 active:tw-bg-grey-400/50 hover:tw-bg-gray-300/50 tw-p-1 tw-rounded tw-z-20 tw-border-none tw-bg-transparent'
                            )}
                            onClick={() => handleUndo()}
                        >
                            <ChevronIcon className="tw-fill-inherit tw-rotate-180 tw-p-[1px]" />
                        </button>
                        <button
                            type="button"
                            title="Redo"
                            className={classNames(
                                'active:tw-fill-blue-600 active:tw-bg-grey-400/50 hover:tw-bg-gray-300/50 tw-p-1 tw-rounded tw-z-20 tw-border-none tw-bg-transparent',
                                redos.length === 0 &&
                                    'tw-fill-gray-300  disabled:tw-bg-transparent disabled:tw-text-gray-300 active:tw-fill-gray-300 active:tw-bg-transparent active:tw-text-gray-300'
                            )}
                            disabled={
                                redos.length === 0 || typeof value === 'string'
                            }
                            onClick={() => handleRedo()}
                        >
                            <ChevronIcon className="tw-fill-inherit tw-p-[1px]" />
                        </button>
                        <button
                            type="button"
                            title="Clear"
                            disabled={signatureData === 0 && value !== ''}
                            className={classNames(
                                'active:tw-fill-blue-600 active:tw-bg-grey-400/50 hover:tw-bg-gray-300/50 tw-p-1 tw-rounded tw-z-20 tw-border-none tw-bg-transparent',
                                signatureData === 0 &&
                                    'tw-fill-gray-300  disabled:tw-bg-transparent disabled:tw-text-gray-300 active:tw-fill-gray-300 active:tw-bg-transparent active:tw-text-gray-300'
                            )}
                            onClick={() => {
                                handleClear();
                                handleDisable(false);
                            }}
                        >
                            <TrashIcon className="tw-fill-inherit" />
                        </button>
                        <button
                            type="button"
                            title="Stop Editing"
                            className={classNames(
                                'active:tw-fill-blue-600 active:tw-bg-grey-400/50 hover:tw-bg-gray-300/50 tw-p-1 tw-rounded tw-z-20 tw-border-none tw-bg-transparent'
                            )}
                            onClick={() => {
                                handleDisable(true);
                            }}
                        >
                            <CloseIcon className="tw-fill-inherit" />
                        </button>
                    </>
                )}
            </div>
            <div className="tw-border-t tw-border-[1px] tw-border-blue-400 tw-border-dashed tw-h-0 tw-absolute tw-w-full tw-mx-auto tw-bottom-1/4 tw-inset-x-0"></div>
            <canvas
                className="tw-aspect-[5/2] tw-w-full tw-border tw-border-gray-500 tw-min-h-40 tw-relative tw-z-10"
                ref={signatureRef}
            />
        </div>
    );
}

SignatureCanvas = React.forwardRef(SignatureCanvas);

function Signature({id, value = '', defaultValue = '', setProps}) {
    const signatureCanvasRef = React.useRef(null);
    const expandedSignatureCanvasRef = React.useRef(null);
    const normalSignatureCanvasRef = React.useRef(null);
    const [signatureData, setSignatureData] = React.useState(0);
    const [signatureValue, setSignatureValue] = React.useState(defaultValue);
    const [expanded, setExpanded] = React.useState(false);
    const [redos, setRedos] = React.useState([]);
    const handleSave = React.useCallback(() => {
        if (signatureCanvasRef.current) {
            setProps({
                value: signatureCanvasRef.current.toDataURL('image/svg+xml'),
            });
        }
    }, [expanded]);
    const handleReset = React.useCallback(() => {
        setSignatureValue(defaultValue);
        handleDisable(true);
        if (signatureCanvasRef.current) {
            signatureCanvasRef.current.clear();
            if (isValidImageDataUri(defaultValue)) {
            signatureCanvasRef.current.fromDataURL(defaultValue);
          }
        }
    }, [expanded, defaultValue]);
    const handleUndo = React.useCallback(() => {
        if (signatureCanvasRef.current) {
            const undo = signatureCanvasRef.current.toData();
            if (undo.length === 0) {
                handleReset();
                setProps({
                    value: defaultValue,
                });
                setSignatureValue(defaultValue)
                return;
            }
            const redo = undo.pop();
            setRedos((prev) => [
                ...prev,
                {...redo, height: oldHeight, width: oldWidth},
            ]);
            signatureCanvasRef.current.fromData(undo);
            setSignatureData(undo.length);
            setSignatureValue(undo);
            setProps({
                  value: signatureCanvasRef.current.toDataURL('image/svg+xml'),
            });
        }
    }, [expanded, defaultValue]);
    const handleRedo = React.useCallback(() => {
        if (signatureCanvasRef.current && redos?.length > 0) {
            const data = signatureCanvasRef.current.toData();
            const redoItem = redos.at(-1);
            const scaledData = scaleDataFrom(
                redoItem,
                signatureCanvasRef.current.signatureCanvas,
                redoItem.height,
                redoItem.width
            );
            data.push(scaledData);
            setRedos((prev) => prev.filter((_, i) => i < prev.length - 1));
            signatureCanvasRef.current.fromData(data);
            setSignatureData(data.length);
            setSignatureValue(data);
            setProps({
                value: signatureCanvasRef.current.toDataURL('image/svg+xml'),
            });
        }
    }, [expanded, redos]);
    const handleClear = React.useCallback(() => {
        if (signatureCanvasRef.current) {
            signatureCanvasRef.current.clear();
            setSignatureData(0);
            setSignatureValue([]);
            setRedos([]);
            setProps({value: ''});
        }
    }, [expanded]);
    const [disabled, setDisabled] = React.useState(isValidImageDataUri(value));
    const handleDisable = React.useCallback(
        (state = false) => {
            if (signatureCanvasRef.current && state === true) {
                signatureCanvasRef.current.off();
                setDisabled(state);
                const data = signatureCanvasRef.current.toData();
                if (data.length === 0){
                    setProps({
                        value: '',
                    });
                } else {
                    setProps({
                        value: signatureCanvasRef.current.toDataURL('image/svg+xml'),
                    });
                }
            } else if (signatureCanvasRef.current && state === false) {
                signatureCanvasRef.current.on();
                setDisabled(state);
                const data = signatureCanvasRef.current.toData();
                if (data.length === 0){
                    setProps({
                        value: '',
                    });
                }else {
                  setProps({
                      value: signatureCanvasRef.current.toDataURL('image/svg+xml'),
                  });
                }
            }
        },
        [expanded]
    );
    //effect to trigger a clear of canvas
    React.useEffect(() => {
        if (value === '') {
            handleClear();
        }
    }, [value]);
    //effect to sync the expanded / normal canvas refs when expanded
    React.useEffect(() => {
        signatureCanvasRef.current = expanded
            ? expandedSignatureCanvasRef.current
            : normalSignatureCanvasRef.current;
        //disable the ability to redo after a maximizing there is a bug that causes the redo to not work properly
        setRedos([]);
    }, [expanded]);
    // effect to sync the value of the signature to the signature canvas
    React.useEffect(() => {
        function escapeEvent(e) {
            if (e.key === 'Escape') {
                setExpanded(false);
            }
        }
        // normalSignatureCanvasRef.current.resizeCanvas()
        document.addEventListener('keydown', escapeEvent);
        return () => {
            document.removeEventListener('keydown', escapeEvent);
        };
    }, []);
    React.useEffect(() => {
      setSignatureValue(defaultValue)
      handleReset()
      setProps({
          value: defaultValue,
      });
    },[defaultValue])
    const [oldWidth, setOldWidth] = React.useState(null);
    const [oldHeight, setOldHeight] = React.useState(null);
    return (
        <div id={id} className="tw-flex tw-m-auto">
            <div className="tw-w-auto">
                <SignatureCanvas
                    ref={normalSignatureCanvasRef}
                    expanded={expanded}
                    disabled={disabled}
                    setExpanded={setExpanded}
                    isExpanded={!expanded}
                    signatureData={signatureData}
                    setSignatureData={setSignatureData}
                    setSignatureValue={setSignatureValue}
                    setRedos={setRedos}
                    redos={redos}
                    value={signatureValue}
                    handleUndo={handleUndo}
                    handleRedo={handleRedo}
                    handleClear={handleClear}
                    handleDisable={handleDisable}
                    handleReset={handleReset}
                    handleSave={handleSave}
                    oldHeight={oldHeight}
                    oldWidth={oldWidth}
                    setOldHeight={setOldHeight}
                    setOldWidth={setOldWidth}
                />
            </div>
        </div>
    );
}

Signature.defaultProps = {};

Signature.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The value displayed in the input.
     */
    value: PropTypes.string,

    /**
     * The default value of the input. Usually a value from the database or an empty string.
     */
    defaultValue: PropTypes.string,
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default Signature;
