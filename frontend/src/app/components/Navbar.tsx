import Link from 'next/link';

export const Navbar = () => {
    return (
        <nav>
            <div className='flex gap-5 ml-8 mt-5'>
                <Link href="/">
                    HOME
                </Link>
                <Link href="/Woman">
                    WOMAN
                </Link>
                <Link href="/Man">
                    MAN
                </Link>
                <Link href="/Suggestions">
                    SUGGESTIONs
                </Link>
            </div>
        </nav>
    );
};

export default Navbar;