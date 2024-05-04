// Navbar.tsx
import Link from 'next/link';

const Navbar = () => {
    return (
        <nav className='text-white' >
            <Link href="/woman">Woman</Link>
            <Link href="/men">Men</Link>
            <Link href="/kids">Kids</Link>
        </nav>
    );
};

export default Navbar;
