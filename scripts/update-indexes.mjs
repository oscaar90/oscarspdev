#!/usr/bin/env node

import { readdirSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const contentDir = join(__dirname, '../client/public/content');
const categories = ['noticias', 'writeups', 'proyectos'];

categories.forEach((category) => {
  const categoryPath = join(contentDir, category);
  
  try {
    const files = readdirSync(categoryPath);
    const slugs = files
      .filter((file) => file.endsWith('.md'))
      .map((file) => file.replace('.md', ''));
    
    const indexPath = join(categoryPath, 'index.json');
    writeFileSync(indexPath, JSON.stringify(slugs, null, 2));
    
    console.log(`✓ Updated ${category}/index.json with ${slugs.length} items`);
  } catch (error) {
    console.error(`✗ Error updating ${category}:`, error.message);
  }
});

console.log('\n✓ All indexes updated successfully');
