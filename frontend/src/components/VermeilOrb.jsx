import React, { useRef, useMemo } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import * as THREE from 'three';

// Simple pseudo-random noise generator for simulation
const noise = (x, y, z, t) => {
    return Math.sin(x * 2.0 + t) * Math.cos(y * 1.5 + t) * Math.sin(z * 3.0 + t * 2.0);
};

const ParticleCloud = ({ state }) => {
    const pointsRef = useRef();
    const originalPositions = useRef();

    // Generate particles
    const particleCount = 5000;

    const [positions, finalPositions] = useMemo(() => {
        const pos = new Float32Array(particleCount * 3);
        for (let i = 0; i < particleCount; i++) {
            // Spherical distribution with varying density
            const theta = Math.random() * Math.PI * 2;
            const phi = Math.acos((Math.random() * 2) - 1);
            const r = 1.5 + (Math.random() * 0.2);

            const x = r * Math.sin(phi) * Math.cos(theta);
            const y = r * Math.sin(phi) * Math.sin(theta);
            const z = r * Math.cos(phi);

            pos[i * 3] = x;
            pos[i * 3 + 1] = y;
            pos[i * 3 + 2] = z;
        }
        return [pos, new Float32Array(pos)]; // Return initial and working copy
    }, []);

    // Store original positions once
    if (!originalPositions.current) {
        originalPositions.current = Float32Array.from(positions);
    }

    useFrame((rootState) => {
        const { clock } = rootState;
        const t = clock.getElapsedTime();

        if (pointsRef.current) {
            // Basic rotation - smooth and constant
            pointsRef.current.rotation.y = t * 0.08;
            pointsRef.current.rotation.z = t * 0.02;

            const geometry = pointsRef.current.geometry;
            const positionAttribute = geometry.attributes.position;
            const currentPositions = positionAttribute.array;
            const origPos = originalPositions.current;

            // Dynamics Configuration
            let ampProxy = 0;     // Amplitude of the "beat"
            let freqProxy = 1.0;  // Frequency/Roughness of the wave
            let speed = 1.0;

            if (state === 'speaking') {
                // Rapid, high-amplitude fluctuation to simulate voice
                // We oscillate amplitude using a fast sine wave
                ampProxy = 0.3 + Math.sin(t * 15) * 0.15 + Math.cos(t * 37) * 0.1;
                freqProxy = 3.0;
                speed = 5.0;
                // Add a "kick" burst effect occasionally
                if (Math.random() > 0.95) ampProxy += 0.2;
            } else if (state === 'listening') {
                // Slow, breathing pulse
                ampProxy = 0.1 + Math.sin(t * 1.5) * 0.05;
                freqProxy = 0.5;
                speed = 1.0;
            } else if (state === 'processing') {
                // Chaotic low-amplitude jitter
                ampProxy = 0.1;
                freqProxy = 10.0;
                speed = 8.0;
            } else {
                // Idle: Gentle ripples
                ampProxy = 0.05;
                freqProxy = 1.0;
                speed = 0.5;
            }

            // Update each particle
            for (let i = 0; i < particleCount; i++) {
                const ix = i * 3;
                const ox = origPos[ix];
                const oy = origPos[ix + 1];
                const oz = origPos[ix + 2];

                // Calculate noise value based on position and time
                // This creates the "wave" patterns moving across the sphere
                const n = noise(ox * freqProxy, oy * freqProxy, oz * freqProxy, t * speed);

                // Displace along the normal vector (which is just the normalized position for a sphere)
                // Ideally we'd normalize, but since it's a sphere centered at 0, position vector is effectively the normal direction
                const displacement = 1 + n * ampProxy;

                currentPositions[ix] = ox * displacement;
                currentPositions[ix + 1] = oy * displacement;
                currentPositions[ix + 2] = oz * displacement;
            }

            positionAttribute.needsUpdate = true;
        }
    });

    const getColor = () => {
        switch (state) {
            case 'speaking': return "#8a2be2"; // Violet
            case 'listening': return "#00ffcc"; // Cyan
            case 'processing': return "#ff00ff"; // Magenta
            default: return "#4b0082"; // Deep Indigo
        }
    }

    // Get opacity based on state (Speaking = brighter/opener)
    const getOpacity = () => {
        return state === 'speaking' ? 0.9 : 0.6;
    }

    return (
        <points ref={pointsRef}>
            <bufferGeometry>
                <bufferAttribute
                    attach="attributes-position"
                    count={particleCount}
                    array={finalPositions} // Use the working copy initial state
                    itemSize={3}
                />
            </bufferGeometry>
            <pointsMaterial
                attach="material"
                color={getColor()}
                size={0.025}
                sizeAttenuation={true}
                transparent={true}
                opacity={getOpacity()}
                blending={THREE.AdditiveBlending}
                depthWrite={false}
            />
        </points>
    );
};

const VermeilOrb = ({ state = 'idle' }) => {
    return (
        <div style={{ height: '400px', width: '100%', position: 'relative' }}>
            {/* Adjusted camera to frame the expanded particles better */}
            <Canvas camera={{ position: [0, 0, 4.0] }}>
                <ambientLight intensity={0.5} />
                <ParticleCloud state={state} />
            </Canvas>
        </div>
    );
};

export default VermeilOrb;
