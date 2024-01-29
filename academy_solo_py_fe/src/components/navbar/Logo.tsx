"use client";
import Image from "next/image";
import Link from "next/link";
import React from "react";

const Logo = () => {
  return (
    <div className="flex flex-shrink-0 items-center">
      <Link href="/" className="-m-1.5 p-1.5">
        <Image
          className="h-8 w-auto"
          src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500"
          alt="Logo"
          width={100}
          height={100}
        />
      </Link>
    </div>
  );
};

export default Logo;
