// next.config.mjs
/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
      remotePatterns: [
        {
          protocol: 'https',
          hostname: 'static.zara.net',
          port: '',
          pathname: '/**',
        },
      ],
    },
  };
  
  export default nextConfig;