/** @type {import('tailwindcss').Config} */
// Tailwind CSS configuration file
// https://tailwindcss.com/docs/configuration
module.exports = {
    // Specify the content files where Tailwind classes are used
    content: ['./src/**/*.{html,js}'],
    // prefix for Tailwind classes so they don't conflict with other CSS frameworks
    prefix: 'tw-',
    // Disable Tailwind's default preflight styles.
    corePlugins: {
        preflight: false,
    },
    theme: {
        extend: {},
    },
    plugins: [],
};
