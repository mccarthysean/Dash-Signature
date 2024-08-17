import React from 'react';
import * as Dialog from '@radix-ui/react-dialog';
import PropTypes from 'prop-types';
import SignaturePad from 'signature_pad';
// output.css is the tailwind css file that is generated from the tailwind.config.js
// This file is generated using the command `npm run css` while in the dash_signature directory.
// Some classes conflict with the existing bootstrap classes. To avoid conflicts, the conflicting classes should be renamed.
// Conflicting classes in this file are currently just `border` which is instead used as `border-[1px]` to avoid conflicts.
import '../css/output.css';
import {ArrowSquareIcon} from '../fragments/ArrowSquareIcon.react';
import * as VisuallyHidden from '@radix-ui/react-visually-hidden';
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
        disabled,
        handleDisable,
        oldHeight,
        oldWidth,
        setOldHeight,
        setOldWidth,
    },
    ref
) {
    console.log('signature canvas', {value, expanded});
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
            resizeCanvas: () => resizeCanvas(),

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
                console.log({data});
                const ctx = canvas.getContext('2d');
                ctx.scale(ratio, ratio);
                setOldHeight(canvas.height);
                setOldWidth(canvas.width);
                signaturePadRef.current.clear();
                if (data && Array.isArray(data)) {
                    console.log('scaling as array');
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
                    console.log({scaledData});
                    setSignatureData(scaledData.length);
                    setSignatureValue(scaledData);
                } else {
                    console.log('scaling as string');
                    if (isValidImageDataUri(value)) {
                        signaturePadRef.current.fromDataURL(value); //.then(() => {
                    }
                }
            }
        },
        [isExpanded]
    );
    const strokeEndEvent = React.useCallback(() => {
        if (ref.current) {
            console.log('stroke end event');
            setSignatureData(signaturePadRef.current.toData().length ?? 0);
            const data = signaturePadRef.current.toData();
            console.log({data});
            setSignatureValue(data);
            setRedos([]);
        }
    }, [value]);
    const size = useWindowSize();
    React.useEffect(() => {
        if (!disabled && signaturePadRef.current) {
            resizeCanvas();
            console.log('size change');
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
        console.log('use effect on signature mount');
        console.log(value);
        if (isValidImageDataUri(value)) {
            resizeCanvas(value);
        } else {
            resizeCanvas(value);
        }
        console.log('done resize effect');
        // Initial resize and scale
        // Load the signature data if it exists
        // if (value.length > 0 && signaturePadRef.current) {
        //   signaturePadRef.current.clear()
        //   signaturePadRef.current.fromDataURL(value).then(() => {
        //     const data = signaturePadRef.current.toData()
        //     signaturePadRef.current.fromData(scaleData(data))
        //   }).catch((e) => {
        //     console.error('something2 went wrong', e)
        //   })
        // } else {
        //   signaturePadRef.current.clear()
        // }
        // Cleanup function to remove the event listener
        return () => {
            // window.removeEventListener('resize', resizeCanvas);
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
        <div className="flex flex-col relative aspect-[5/2]">
            {/* <button type='button' title='Maximize' className={classNames('active:fill-blue-600 active:bg-grey-400/50 hover:bg-gray-300/50 absolute flex top-0 p-1 rounded z-20 bg-white right-0 m-2')}
        onClick={
          () => {
            setExpanded(!expanded)
          }

        }>
        <ArrowSquareIcon className={classNames('fill-inherit transition', expanded && 'rotate-180')} />
      </button> */}
            <div className="absolute z-20 flex bottom-0 right-0 p-1 justify-end gap-2">
                {disabled ? (
                    <button
                        type="button"
                        title="Edit"
                        className={classNames(
                            'active:fill-blue-600 active:bg-grey-400/50 hover:bg-gray-300/50 p-1 rounded z-20 bg-white'
                        )}
                        onClick={() => handleDisable(false)}
                    >
                        <EditIcon className="fill-inherit p-[1px]" />
                    </button>
                ) : (
                    <>
                        <button
                            type="button"
                            title="Undo"
                            // disabled={redos.length === 0 || typeof value === 'string'}
                            className={classNames(
                                'active:fill-blue-600 active:bg-grey-400/50 hover:bg-gray-300/50 p-1 rounded z-20 bg-white'
                            )}
                            onClick={() => handleUndo()}
                        >
                            <ChevronIcon className="fill-inherit rotate-180 p-[1px]" />
                        </button>
                        <button
                            type="button"
                            title="Redo"
                            className={classNames(
                                'active:fill-blue-600 active:bg-grey-400/50 hover:bg-gray-300/50 p-1 rounded z-20 bg-white',
                                redos.length === 0 &&
                                    'fill-gray-300  disabled:bg-transparent disabled:text-gray-300 active:fill-gray-300 active:bg-transparent active:text-gray-300'
                            )}
                            disabled={
                                redos.length === 0 || typeof value === 'string'
                            }
                            onClick={() => handleRedo()}
                        >
                            <ChevronIcon className="fill-inherit p-[1px]" />
                        </button>
                        <button
                            type="button"
                            title="Clear"
                            disabled={signatureData === 0 && value !== ''}
                            className={classNames(
                                'active:fill-blue-600 active:bg-grey-400/50 hover:bg-gray-300/50 p-1 rounded z-20 bg-white',
                                signatureData === 0 &&
                                    'fill-gray-300  disabled:bg-transparent disabled:text-gray-300 active:fill-gray-300 active:bg-transparent active:text-gray-300'
                            )}
                            onClick={() => {
                                handleClear();
                                handleDisable(false);
                            }}
                        >
                            <TrashIcon className="fill-inherit" />
                        </button>
                        <button
                            type="button"
                            title="Stop Editing"
                            className={classNames(
                                'active:fill-blue-600 active:bg-grey-400/50 hover:bg-gray-300/50 p-1 rounded z-20 bg-white'
                            )}
                            onClick={() => {
                                handleDisable(true);
                            }}
                        >
                            <CloseIcon className="fill-inherit" />
                        </button>
                    </>
                )}
            </div>
            <div className="border-t border-[1px] border-blue-400 border-dashed h-0 absolute w-full mx-auto bottom-1/4 inset-x-0"></div>
            <canvas
                className="aspect-[5/2] w-full border border-gray-500 min-h-40 relative z-10"
                ref={signatureRef}
            />
        </div>
    );
}

SignatureCanvas = React.forwardRef(SignatureCanvas);

function Signature({id, value = '', save = false, resize = false, setProps}) {
    const signatureCanvasRef = React.useRef(null);
    const expandedSignatureCanvasRef = React.useRef(null);
    const normalSignatureCanvasRef = React.useRef(null);
    const [signatureData, setSignatureData] = React.useState(0);
    const [signatureValue, setSignatureValue] = React.useState(value);
    const [expanded, setExpanded] = React.useState(false);
    const [redos, setRedos] = React.useState([]);
    const handleSave = React.useCallback(() => {
        if (signatureCanvasRef.current) {
            setProps({
                value: signatureCanvasRef.current.toDataURL('image/svg+xml'),
                save: false,
            });
        }
    }, [expanded]);
    const handleReset = React.useCallback(() => {
        console.log({resetValue: value});
        setSignatureValue(value);
        handleDisable(true);
        if (signatureCanvasRef.current) {
            signatureCanvasRef.current.clear();
            signatureCanvasRef.current.fromDataURL(value);
        }
    }, [expanded]);
    const handleUndo = React.useCallback(() => {
        if (signatureCanvasRef.current) {
            const undo = signatureCanvasRef.current.toData();
            console.log({beforeUndo: undo});
            if (undo.length === 0) {
                handleReset();
                return;
            }
            const redo = undo.pop();
            console.log({afterUndo: undo});
            setRedos((prev) => [
                ...prev,
                {...redo, height: oldHeight, width: oldWidth},
            ]);
            signatureCanvasRef.current.fromData(undo);
            setSignatureData(undo.length);
            const undoData = signatureCanvasRef.current.toData();
            setSignatureValue(undo);
        }
    }, [expanded]);
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
        }
    }, [expanded, redos]);
    const handleClear = React.useCallback(() => {
        if (signatureCanvasRef.current) {
            signatureCanvasRef.current.clear();
            setSignatureData(0);
            setSignatureValue([]);
            setRedos([]);
        }
    }, [expanded]);
    const [disabled, setDisabled] = React.useState(isValidImageDataUri(value));
    const handleDisable = React.useCallback(
        (state = false) => {
            console.log({signatureCanvasRef});
            if (signatureCanvasRef.current && state === true) {
                signatureCanvasRef.current.off();
                console.log('here');
                setDisabled(state);
            } else if (signatureCanvasRef.current && state === false) {
                signatureCanvasRef.current.on();
                console.log('here');
                setDisabled(state);
            }
        },
        [expanded]
    );
    //effect to trigger save of value
    React.useEffect(() => {
        if (save) {
            handleSave();
        }
    });
    //effect to trigger a clear of canvas
    React.useEffect(() => {
        if (value === '') {
            handleClear();
        }
    }, [value]);
    //effect to trigger a resize of the canvas on btn click
    React.useEffect(() => {
        if (resize) {
            signatureCanvasRef.current.resizeCanvas();
            setProps({resize: false});
        }
    });
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
    const [oldWidth, setOldWidth] = React.useState(null);
    const [oldHeight, setOldHeight] = React.useState(null);
    return (
        <div id={id} className="flex m-auto">
            {/* <Dialog.Root open={expanded}>
        <Dialog.Portal >
          <Dialog.Overlay className='fixed inset-0 z-40 flex bg-black/20' />
          <Dialog.Content className='bg-white md:rounded-lg md:p-3 z-50 fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-full md:w-[90vw] max-h-[85vh]'>
            <VisuallyHidden.Root asChild>
              <Dialog.Title className='flex justify-between items-center'>Signature</Dialog.Title>
            </VisuallyHidden.Root>
            <VisuallyHidden.Root asChild>
              <Dialog.Description>Signature Pad</Dialog.Description>
            </VisuallyHidden.Root>
            <SignatureCanvas
              ref={expandedSignatureCanvasRef}
              expanded={expanded}
              disabled={disabled}
              setExpanded={setExpanded}
              isExpanded={expanded}
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
              oldHeight={oldHeight}
              oldWidth={oldWidth}
              setOldHeight={setOldHeight}
              setOldWidth={setOldWidth}
            />
          </Dialog.Content>
        </Dialog.Portal>
      </Dialog.Root> */}
            <div className="w-auto">
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
     * The trigger for the component to update the value.
     * Setting to true will update the value.
     */
    save: PropTypes.bool,
    resize: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default Signature;
