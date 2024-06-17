import { Poses } from "@/lib/constants"
import Image from "next/image"
import * as images from '@/lib/assets/poses'

const imageMap: any = {
    [Poses.HIGH_BRIDGE]: <Image src={images.high_bridge_image} alt={'high-bridge'} className={'object-contain w-full h-full'} priority/>,
    [Poses.HANDS_TO_TOES]: <Image src={images.hands_to_toes_image} alt={'high-bridge'} className={'object-contain w-full h-full'} priority/>,
    [Poses.JUMPING_JACK]: <Image src={images.jumping_jack_image} alt={'high-bridge'} className={'object-contain w-full h-full'} priority/>,
    [Poses.LUNGE_HANDS_UP]: <Image src={images.lunge_hands_up_image} alt={'high-bridge'} className={'object-contain w-full h-full'} priority/>,
    [Poses.ONE_LEG_STAND]: <Image src={images.one_leg_stand_image} alt={'high-bridge'} className={'object-contain w-full h-full'} priority/>,
    [Poses.DEEP_SQUAT]: <Image src={images.deep_squat_image} alt={'high-bridge'} className={'object-contain w-full h-full'} priority/>,
    [Poses.PLANK]: <Image src={images.plank_image} alt={'high-bridge'} className={'object-contain w-full h-full'} priority/>,
}

const PoseImage = ({ pose }: { pose: Poses }) => {
    return (
        <>{imageMap[pose]}</>
    )
} 

export default PoseImage