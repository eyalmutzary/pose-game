import React, { FC } from "react";
import Container from "./Container";

type ButtonProps = {
    children: React.ReactNode;
    onClick: () => void;
};

export const Button: FC<ButtonProps> = ({ children, onClick }) => {
    return (
        <Container onClick={onClick} className="text-[1.5em] text-center min-w-48 font-bold cursor-pointer">
            {children}
        </Container>
    );
};
