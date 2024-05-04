// Navbar.js
import Link from 'next/link';

const Layaout = ({children}: {children: JSX.Element | JSX.Element[] } ) => {
    return (
        <main>
        <nav className='text-white' >
                    <Link href="/woman">
                        <a>Woman</a>
                    </Link>
                    <Link href="/men">
                        <a>Men</a>
                    </Link>
                    <Link href="/kids">
                        <a>Kids</a>
                    </Link>
        </nav>
        {children}
    </main>
    );
};

export default Layaout;
